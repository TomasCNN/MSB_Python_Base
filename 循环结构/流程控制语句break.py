# 流程控制语句break
# 用于结束循环结构，通常与分支结构if一起使用


'''在键盘录入密码，最多录入3次。如果正确就结束循环'''
for i in range(3):
    password = input('Password:')
    if password == '123456':
        print("密码正确！")
        break
    else:
        print('密码错误！')


a = 0
while a < 3:
    password1 = input('Password1:')
    if password1 == '654321':
        print("密码正确！")
        break
    else:
        print('密码错误！')
    a += 1