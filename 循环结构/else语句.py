# else语句
'''
    与else语句配合使用的三种情况
    if ……：
    ……
    else：
    ……

    for ……：
    ……
    else：
    ……

    while ……：
    ……
    else：
    ……

    第一种情况，if条件表达式搬出来时执行else
    第二种第三种情况，没有碰到break时执行else语句

'''



for i in range(3):
    password = input('Password:')
    if password == '123456':
        print("密码正确！")
        break
    else:
        print('密码错误！')
else:
    print('抱歉，三次输入密码均错误！')


a = 0
while a < 3:
    password1 = input('Password1:')
    if password1 == '654321':
        print("密码正确！")
        break
    else:
        print('密码错误！')
    a += 1
else:
    print('抱歉，三次输入密码均错误！')