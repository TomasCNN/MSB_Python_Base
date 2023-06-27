# 数据类型转换

# 为什么要进行数据类型转换？ 将不同数据类型的数据拼接到一起

#函 数	作 用
# int(x)	将 x 转换成整数类型
# float(x)	将 x 转换成浮点数类型
# complex(real，[,imag])	创建一个复数
# str(x)	将 x 转换为字符串
# repr(x)	将 x 转换为表达式字符串
# eval(str)	计算在字符串中的有效 Python 表达式，并返回一个对象
# chr(x)	将整数 x 转换为一个字符
# ord(x)	将一个字符 x 转换为它对应的整数值
# hex(x)	将一个整数 x 转换为一个十六进制字符串
# oct(x)	将一个整数 x 转换为一个八进制的字符串

int("123") #转换成功
# int("123个")  # 转换失败



# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，一般情况下你只需要将数据类型作为函数名即可。
#
# Python 数据类型转换可以分为两种：
#
# 隐式类型转换 - 自动完成
# 显式类型转换 - 需要使用类型函数来转换
# 隐式类型转换
# 在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
#
# 以下实例中，我们对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失。


num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

# 代码解析：
#
# 实例中我们对两个不同数据类型的变量 num_int 和 num_flo 进行相加运算，并存储在变量 num_new 中。
# 然后查看三个变量的数据类型。
# 在输出结果中，我们看到 num_int 是 整型（integer） ， num_flo 是 浮点型（float）。
# 同样，新的变量 num_new 是 浮点型（float），这是因为 Python 会将较小的数据类型转换为较大的数据类型，以避免数据丢失。

# um_int = 123
# um_str = "456"

# rint("Data type of num_int:",type(num_int))
# rint("Data type of num_str:",type(num_str))

# print(num_int+num_str)

# 以上实例输出结果为：
#
# num_int 数据类型为: <class 'int'>
# num_str 数据类型为: <class 'str'>
# Traceback (most recent call last):
#   File "/runoob-test/test.py", line 7, in <module>
#     print(num_int+num_str)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 从输出中可以看出，整型和字符串类型运算结果会报错，输出 TypeError。 Python 在这种情况下无法使用隐式转换。
#
# 但是，Python 为这些类型的情况提供了一种解决方案，称为显式转换。

# 显式类型转换

# 在显式类型转换中，用户将对象的数据类型转换为所需的数据类型。 我们使用 int()、float()、str() 等预定义函数来执行显式类型转换。
#

# int() 强制转换为整型：
x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3
print("x = ",x)
print("y = ",y)
print("z = ",z)

# float() 强制转换为浮点型：

x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2
print("x = ",x)
print("y = ",y)
print("z = ",z)
print("w = ",w)

# str() 强制转换为字符串类型：

x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'
print("x = ",x)
print("y = ",y)
print("z = ",z)

num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))

# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
#
# 函数	描述
# int(x [,base])           将x转换为一个整数
# float(x)                 将x转换到一个浮点数
# complex(real [,imag])    创建一个复数
# str(x)                   将对象 x 转换为字符串
# repr(x)                  将对象 x 转换为表达式字符串
# eval(str)                用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)                 将序列 s 转换为一个元组
# list(s)                  将序列 s 转换为一个列表
# set(s)                   转换为可变集合
# dict(d)                  创建一个字典。d 必须是一个 (key, value)元组序列。
# frozenset(s)             转换为不可变集合
# chr(x)                   将一个整数转换为一个字符
# ord(x)                   将一个字符转换为它的整数值
# hex(x)                   将一个整数转换为一个十六进制字符串
# oct(x)                   将一个整数转换为一个八进制字符串

name = 'Tomas'
age = 25

print(type(name),type(age))                              # 说明name与age的数据类型不相同
# print('我叫' + name + '今年' + age + '岁')              # 当将str类型与int类型进行连接时，报错；解决方案：类型转换
print('我叫' + name + '今年' + str(age) + '岁')           # 将int类型数据通过str()函数转换成str类型

print('--------------------------------str()将其他数据类型转换为str数据类型--------------------------------')
a = 10
b = 198.8
c = False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(a)),type(str(a)))

print('--------------------------------int()将其他数据类型转换为int数据类型--------------------------------')
d = '10'
e = 198.8
f = '198.8'
g = False
h = 'Hello'
print(type(d),type(e),type(f),type(g),type(h))
print(int(d),type(int(d)))                              # 将str类型转换为int类型，字符串为数字串
print(int(e),type(int(e)))                              # 将float类型转换为int类型，截取整数部分，舍去小数部分
# print(int(f),type(int(f)))                            # 将str类型转换为int类型，报错，因为字符串为小数串
print(int(g),type(int(g)))                              #
# print(int(h),type(int(h)))                            # 将str类型转换为int类型，字符串必须为数字串（整数），非数字串是不允许转换的


print('--------------------------------float()将其他数据类型转换为float数据类型--------------------------------')
d = '10'
e = 198.8
f = '198.8'
g = False
h = 'Hello'
print(type(d),type(e),type(f),type(g),type(h))
print(float(d),type(float(d)))                              #
print(float(e),type(float(e)))                              #
print(float(f),type(float(f)))                              #
print(float(g),type(float(g)))                              #
# print(int(h),type(float(h)))                              # 字符串中的数据如果是非数字串，则不允许转换