from typing import Optional

import urllib3
from outline_api import Manager

import src.settings as settings
from src.classes import OutlineUser
from src.db import Admin, User, session

urllib3.disable_warnings()

apiurl = settings.APIURL
apicert = settings.APICERT

manager = Manager(apiurl=apiurl, apicrt=apicert)

data_usage: dict = manager.all_active()


def keydict_to_outlineuser(dict: dict,) -> OutlineUser:
    outlineuser = OutlineUser()
    for key in dict.keys():
        if hasattr(outlineuser, key):
            setattr(outlineuser, key, dict[key])
    if hasattr(outlineuser, 'data_usage'):
        setattr(outlineuser, 'data_usage', data_usage.get(outlineuser.id))

    admin = Admin(admin_tg_id=settings.BOT_ADMIN)
    if not session.query(Admin).filter(
            Admin.admin_tg_id == settings.BOT_ADMIN
    ).all():
        session.add(admin)
        session.commit()
    admin_id = session.query(Admin).filter(
        Admin.admin_tg_id == settings.BOT_ADMIN
    ).first().id
    user_db = User(
        id=outlineuser.id,
        name=outlineuser.name,
        password=outlineuser.password,
        port=outlineuser.port,
        method=outlineuser.method,
        accessUrl=outlineuser.accessUrl,
        data_usage=outlineuser.data_usage,
        admin_tg_id=admin_id
    )
    if not session.query(User).filter(User.id == outlineuser.id).all():
        session.add(user_db)
        session.commit()
    return outlineuser


def get_all_users() -> Optional[list[OutlineUser]]:
    global data_usage
    data_usage = manager.all_active()
    all_keys = manager.all()
    return [keydict_to_outlineuser(key) for key in all_keys]


def get_new_user(label: Optional[str] = None) -> OutlineUser:
    new_user: dict = manager.new()
    if label:
        manager.rename(new_user.get('id'), label)
        new_user.update({'name': label})
    return keydict_to_outlineuser(new_user)
