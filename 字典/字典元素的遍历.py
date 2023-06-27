'''
    字典元素的遍历
    for item in socres:
        print (item)
'''

scores = {'张三': 100, '李四': 200, '王五': 250}
print(scores)
print(type(scores))
print(id(scores))

# 字典元素的遍历
for item in scores:
    print(item)
    print(item,scores[item])
    print(item,scores.get(item))