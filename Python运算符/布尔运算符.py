# 布尔运算符

# and 当两个运算符都为True时,运算结果才为True
# or 只要有一个运算符为True时,运算结果就为True

# not 如果运算数为True,运算结果为False
#     如果运算数为False,运算结果为True

a,b = 1,2
print(a == 1 and b == 2)
print(a == 1 and b < 2)
print(a != 1 and b == 2)
print(a != 1 and b != 2)


print(a == 1 or b == 2)
print(a == 1 or b < 2)
print(a != 1 or b == 2)
print(a != 1 or b != 2)


F = 0;
T = 1;
print(not T)
print(not F)