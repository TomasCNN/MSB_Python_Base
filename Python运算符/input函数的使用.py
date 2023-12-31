# input函数的使用

# input函数
# 作用：接收来自用户的输入
# 返回值类型：输入值的类型为str
# 值的存储：使用“=”对输入的值进行存储

# Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
#
# Python2.x 中 input() 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入。
#
# raw_input() 将所有输入作为字符串看待，返回字符串类型。
# 而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）。


# 注意：input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
# 而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
#
# 除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
#
# 注意：python3 里 input() 默认接收到的是 str 类型。

# Python2.x: input() 需要输入 python 表达式
a = input("input:")                       # 输入整数
print(type(a))                            # 整型
a = input("input:")                       # 正确，字符串表达式
print(type(a))                            # 字符串
a = input("input:")                       # 报错，不是表达式
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<string>", line 1, in <module>
# NameError: name 'runoob' is not defined
# <type 'str'>

# Python2.x: raw_input() 将所有输入作为字符串看待
# a = raw_input("input:")
# print(type(a))                            # 字符串+

# a = raw_input("input:")
# print(type(a))                            # 字符串

