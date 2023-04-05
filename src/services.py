from src.classes import OutlineUser


def print_outline_users(userlist: list[OutlineUser] | OutlineUser) -> str:
    if type(userlist) is OutlineUser:
        userlist = [userlist, ]

    if userlist is None:
        return ''

    response = ''
    for user in userlist:
        if user.data_usage:
            user.data_usage = round(user.data_usage / 1048576)
        response += (f'id: {user.id}\n'
                     f'name: {user.name}\n'
                     f'password: {user.password}\n'
                     f'port: {user.port}\n'
                     f'method: {user.method}\n'
                     f'accessUrl: {user.accessUrl}\n'
                     f'data_usage: {user.data_usage} MB\n'
                     f'\n')
    return response
