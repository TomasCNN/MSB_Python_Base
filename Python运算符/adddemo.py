# 从键盘输入两个整数,计算两个整数的和.
a = input("请输入一个加数:")
b = input("请输入另一个加数:")
print(type(a),type(b))
print(a+b)    # 此时加号的作用是将字符a和字符串b拼接到一起
# 类型转换:如果需要整数型和浮点型,就需要将str类型通过int()函数或者float()函数进行数据类型转换.
#

print(int(a)+int(b))
print(float(a)+float(b))
print(str(a)+str(b))
print(bool(a)+bool(b))
print(type(int(a)+int(b)))
print(type(float(a)+float(b)))
print(type(str(a)+str(b)))
print(type(bool(a)+bool(b)))
print(type(type(int(a)+int(b))))
print(type(type(float(a)+float(b))))
print(type(type(str(a)+str(b))))
print(type(type(bool(a)+bool(b))))
print(type(type(type(int(a)+int(b)))))
print(type(type(type(float(a)+float(b)))))
print(int(a)+int(b))

# 方式二:
# a = input("请输入一个加数:")
# a = int(a)
# b = input("请输入另一个加数:")
# b = int(b)
# print(type(a),type(b))
# print(a+b)    # 此时加号的作用是将字符a和字符串b拼接到一起