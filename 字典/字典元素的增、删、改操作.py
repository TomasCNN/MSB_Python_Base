'''
    # 字典元素的增、删、改操作
    key 的判断
    1. in -----> 指定的key在字典中存在返回True -----> '张三' in scores
    2. not in -----> 指定的key在字典中不存在返回True -----> '张四' not in scores
    字典元素的删除
    del scores['张三']
    字典元素的新增
    scores['jack''] = 120
'''


scores = {'张三': 100, '李四': 200, '王五': 250}
print(scores)
print(type(scores))
print(id(scores))


print('张三' in scores)
print('张四' not in scores)

# 删除指定的key-Value对
del scores['张三']
print(scores)

# 清空字典的元素
scores.clear()
print(scores)

# 新增字典元素
scores['jack'] = 120
print(scores)

# 修改字典元素
scores['jack'] = 250
print(scores)