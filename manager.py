from typing import Optional

from outline_api import (
    Manager)
import urllib3

from classes import OutlineUser
import settings

urllib3.disable_warnings()

apiurl = settings.APIURL
apicert = settings.APICERT

manager = Manager(apiurl=apiurl, apicrt=apicert)


def keydict_to_outlineuser(dict: dict,) -> OutlineUser:
    data_usage: dict = manager.all_active()
    outlineuser = OutlineUser()
    for key in dict.keys():
        if hasattr(outlineuser, key):
            setattr(outlineuser, key, dict[key])
    if hasattr(outlineuser, 'data_usage'):
        setattr(outlineuser, 'data_usage', data_usage.get(outlineuser.id))
    return outlineuser


def get_all_users() -> Optional[list[OutlineUser]]:
    all_keys = manager.all()
    return [keydict_to_outlineuser(key) for key in all_keys]


def get_new_user(label: Optional[str] = None) -> OutlineUser:
    new_user: dict = manager.new()
    if label:
        manager.rename(new_user.get('id'), label)
        new_user.update({'name': label})
    return keydict_to_outlineuser(new_user)


# print(get_all_users())
# last = manager.all()[1]
# print(last)
# print(keydict_to_outlineuser(last))
# print(OutlineUser.__match_args__)
# print(get_new_user('яяя'))
