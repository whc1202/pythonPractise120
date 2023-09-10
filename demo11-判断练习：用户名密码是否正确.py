# 判断练习：用户名和密码是否正确

import getpass  # 导入模块
username = input("username:")
password = getpass.getpass("password:")
if username=='charlie' and password == '11223344a':
    print('你的账号密码输入正确')
else:
    print('账号密码输入错误！')