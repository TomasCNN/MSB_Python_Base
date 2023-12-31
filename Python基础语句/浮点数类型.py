# 浮点数类型

# Python 中的小数有两种书写形式：
# 1) 十进制形式
# 这种就是我们平时看到的小数形式，例如 34.6、346.0、0.346。
#
# 书写小数时必须包含一个小数点，否则会被 Python 当作整数处理。
# 2) 指数形式
# Python 小数的指数形式的写法为：
# aEn 或 aen
#
# a 为尾数部分，是一个十进制数；n 为指数部分，是一个十进制整数；E或e是固定的字符，用于分割尾数部分和指数部分。
#  整个表达式等价于 a×10n。
#
# 指数形式的小数举例：
# 2.1E5 = 2.1×105，其中 2.1 是尾数，5 是指数。
# 3.7E-2 = 3.7×10-2，其中 3.7 是尾数，-2 是指数。
# 0.5E7 = 0.5×107，其中 0.5 是尾数，7 是指数。
#
# 注意，只要写成指数形式就是小数，即使它的最终值看起来像一个整数。例如 14E3 等价于 14000，但 14E3 是一个小数。

# Python 只有一种小数类型，就是 float。C语言有两种小数类型，分别是 float 和 double：
# float 能容纳的小数范围比较小，double 能容纳的小数范围比较大。


# 【实例】小数在 Python 中的使用：

f1 = 12.5
print("f1Value: ", f1)
print("f1Type: ", type(f1))
f2 = 0.34557808421257003
print("f2Value: ", f2)
print("f2Type: ", type(f2))
f3 = 0.0000000000000000000000000847
print("f3Value: ", f3)
print("f3Type: ", type(f3))
f4 = 345679745132456787324523453.45006
print("f4Value: ", f4)
print("f4Type: ", type(f4))
f5 = 12e4
print("f5Value: ", f5)
print("f5Type: ", type(f5))
f6 = 12.3 * 0.1
print("f6Value: ", f6)
print("f6Type: ", type(f6))

# 运行结果：
# f1Value:  12.5
# f1Type:  <class 'float'>
# f2Value:  0.34557808421257
# f2Type:  <class 'float'>
# f3Value:  8.47e-26
# f3Type:  <class 'float'>
# f4Value:  3.456797451324568e+26
# f4Type:  <class 'float'>
# f5Value:  120000.0
# f5Type:  <class 'float'>
# f6Value:  1.2300000000000002
# f6Type:  <class 'float'>
#
# 从运行结果可以看出，Python 能容纳极小和极大的浮点数。print 在输出浮点数时，会根据浮点数的长度和大小适当的舍去一部分数字，或者采用科学计数法。
#
# f5 的值是 120000，但是它依然是小数类型，而不是整数类型。
#
# 让人奇怪的是 f6，12.3*0.1的计算结果很明显是 1.23，但是 print 的输出却不精确。
# 这是因为小数在内存中是以二进制形式存储的，小数点后面的部分在转换成二进制时很有可能是一串无限循环的数字，
# 无论如何都不能精确表示，所以小数的计算结果一般都是不精确的。

# 浮点数由整数部分与小数部分组成
# 浮点数的存储存在不精确性，使用浮点数进行计算时，可能会出现小数位数不确定的情况。
# 解决方案：导入模块decimal+
from decimal import Decimal
print(1.1 + 2.2)
print(1.1 + 2.1)
print(Decimal('1.1') + Decimal('2.2'))
