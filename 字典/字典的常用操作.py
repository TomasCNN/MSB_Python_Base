'''
    # 字典的常用操作
    1.字典中元素的获取
        [] : 举例：socres['张三']
        get()方法:举例：scores.get('张三')
    []取值与使用get()取值的区别
    []如果字典中不存在指定的key，抛出KeyError异常；
    get()方法取值，如果字典中不存在指定的key,并不会抛出KeyError而是返回None，可以通过参数设置默认的value，以便指定的key不存在时返回。

'''

scores = {'张三': 100, '李四': 200, '王五': 250}
print(scores)
print(type(scores))
print(id(scores))


'''第一种方法，使用[]'''
print(scores['张三'])
# print(scores['张四']) # 报错：KeyError: '张四'

'''第一种方法，使用get()方法'''
print(scores.get('李四'))
print(scores.get('张四'))

# 110是在查找'张四'所对的Value不存在时，提供的一个默认值。
print(scores.get('张四',110))