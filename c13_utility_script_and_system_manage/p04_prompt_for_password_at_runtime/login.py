import getpass

user = getpass.getuser()
passwd = getpass.getpass()


def login(user, passwd):
    return user == passwd


if login(user, passwd):
    print('yes')
else:
    print('no')
