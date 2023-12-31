# 进制数

# 在 Python 中，可以使用多种进制来表示整数：
# 1) 十进制形式
# 我们平时常见的整数就是十进制形式，它由 0~9 共十个数字排列组合而成。
#
# 注意，使用十进制形式的整数不能以 0 作为开头，除非这个数值本身就是 0。
# 2) 二进制形式
# 由 0 和 1 两个数字组成，书写时以0b或0B开头。例如，101 对应十进制数是 5。
# 3) 八进制形式
# 八进制整数由 0~7 共八个数字组成，以0o或0O开头。注意，第一个符号是数字 0，第二个符号是大写或小写的字母 O。
#
# 在 Python 2.x 中，八进制数字还可以直接以0（数字零）开头。
# 4) 十六进制形式
# 由 0~9 十个数字以及 A~F（或 a~f）六个字母组成，书写时以0x或0X开头，

#十六进制
hex1 = 0x45
hex2 = 0x4Af
print("hex1Value: ", hex1)
print("hex2Value: ", hex2)
#二进制
bin1 = 0b101
print('bin1Value: ', bin1)
bin2 = 0B110
print('bin2Value: ', bin2)
#八进制
oct1 = 0o26
print('oct1Value: ', oct1)
oct2 = 0O41
print('oct2Value: ', oct2)
