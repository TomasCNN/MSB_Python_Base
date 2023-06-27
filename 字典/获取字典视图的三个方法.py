'''
    # 获取字典视图的三个方法
    keys（）:获取字典中的所有key
    values()：获取字典中的所有value
    items()：获取字典中的所有key，value对
'''

scores = {'张三': 100, '李四': 200, '王五': 250}
print(scores)
print(type(scores))
print(id(scores))

# 获取字典中的所有key
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))

# 获取字典中的所有value
values = scores.values()
print(values)
print(type(values))
print(list(values))

# 获取字典中的所有key，value对
items = scores.items()
print(items)
print(type(items))
print(list(items))