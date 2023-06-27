# 对象的布尔值
# Python一切皆对象，所有对象都有一个布尔值
# 获取对象的布尔值
# 使用内置函数bool())
#


# 以下对象的布尔值为False
'''
    False
    数值0
    None
    空字符串
    空列表
    空元组
    空字典
    空集合
'''

# 测试对象的布尔值
print(bool(False))          # False
print(bool(0))              # False
print(bool(0.0))            # False
print(bool(None))           # False
print(bool(''))             # False
print(bool(""))             # False
print(bool([]))             # False-空列表
print(bool(list()))         # False-空列表
print(bool(()))             # False-空元组
print(bool(tuple()))        # False-空元组
print(bool({}))             # False-空字典
print(bool(dict()))         # False-空字典
print(bool(set()))          # False-空集合
print("---------------------------以上对象的布尔值均为False---------------------------")
print("---------------------------其他对象的布尔值均为True ---------------------------")
print(bool(18))
print(bool(True))
print(bool('Hello_World'))