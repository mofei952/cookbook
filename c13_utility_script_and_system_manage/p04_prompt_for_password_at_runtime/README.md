# 允许时弹出密码输入提示

使用Python的 getpass 模块，可以很轻松的弹出密码输入提示，并且不会在用户终端回显密码。代码如下：
```sh
import getpass

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):
   print('Yay!')
else:
   print('Boo!')
```

getpass.getuser() 不会弹出用户名的输入提示。 它会根据该用户的shell环境或者会依据本地系统的密码库（支持 pwd 模块的平台）来使用当前用户的登录名。