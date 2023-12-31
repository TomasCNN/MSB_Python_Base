# 位运算符
# 将数据转化成二进制进行计算
# 位与&:对应数位都是1,结果数位才是1,否则为0
# 位或|:对应数位都是0,结果数位才是0,否则为1
# 左移位运算符<<:高位溢出舍弃,底位补0  (高位截断,底位补0)
# 右移位运算符>>:底位溢出舍弃,高位补0  (高位补0,底位截断)

print(4 & 8)    # 按位与& 同为1时,结果为1
print(5 | 8)    # 按位或| 同为0时,结果为0
print(4 << 1)   # 向左移动1位(移动一个位置),相当于乘以2
print(4 << 2)   # 向左移动2位(移动一个位置),相当于乘以4

print(4 >> 1)   # 向右移动1位(移动一个位置),相当于除以2
print(4 >> 2)   # 向右移动2位(移动一个位置),相当于除以4