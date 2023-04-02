from app.classes import OutlineUser


def print_outline_users(userlist: list[OutlineUser] | OutlineUser) -> str:
    if type(userlist) is OutlineUser:
        userlist = [userlist, ]

    if userlist is None:
        return ''

    response = ''
    for user in userlist:
        response += (f'id: {user.id}\n'
                     f'name: {user.name}\n'
                     f'password: {user.password}\n'
                     f'port: {user.port}\n'
                     f'method: {user.method}\n'
                     f'accessUrl: {user.accessUrl}\n'
                     f'data_usage: {user.data_usage}\n'
                     f'\n')
    return response
