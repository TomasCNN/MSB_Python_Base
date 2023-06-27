# 数据类型

# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
#
# 等号（=）用来给变量赋值。
#
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。

# 文本类型：	str
# 数值类型：	int, float, complex
# 序列类型：	list, tuple, range
# 映射类型：	dict
# 集合类型：	set, frozenset
# 布尔类型：	bool
# 二进制类型：	bytes, bytearray, memoryview

# Python允许你同时为多个变量赋值。例如：
# a = b = c = 1
# 以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
#
# 您也可以为多个对象指定多个变量。例如：
# a, b, c = 1, 2, "runoob"
# 以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

# 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
# 2、一个变量可以通过赋值指向不同类型的对象。
# 3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
# 4、在混合计算时，Python会把整型转换成为浮点数。
# 5、Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj，或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。

# Number（数字）
# Python3 支持 int、float、bool、complex（复数）。
#
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
#
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
#
# 内置的 type() 函数可以用来查询变量所指的对象类型。

name = 'Johnson'
print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# Python3 中有六个标准的数据类型：
#
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
#
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# 为了提高数字的的可读性，Python 3.x 允许使用下划线_作为数字（包括整数和小数）的分隔符。通常每隔三个数字添加一个下划线，类似于英文数字中的逗号。下划线不会影响数字本身的值。
#
# 【实例】使用下划线书写数字：

click = 1_301_547
distance = 384_000_000
print("Python教程阅读量：", click)
print("地球和月球的距离：", distance)

