# for-in循环
'''
# for-in循环
    1.in表达从（字符串、序列等）中依次取值，又称为便利
    2.for-in遍历的对象必须是可迭代对象
# for-in的语法结构
    for 自定义的变量 in 可迭代对象
        循环体
# 循环体内不需要访问自定义变量，可以将自定义变量替代为下划线

'''

for item in  'Python':         # 第一次取出来的是P，将P赋值给item，将item的值输出
    print(item)

# range())产生一个整数序列，也是一个可迭代对象
for i in  range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为"_"
for _ in range(10):
    print('China Number One!')

'''使用for循环，计算1-100之间的偶数和'''
print('----------------使用for循环，计算1-100之间的偶数和--------------------------------')
sum = 0
for j in range(1,101):
    if j % 2 == 0:
        sum += j
print('1-100之间的偶数和为',sum)