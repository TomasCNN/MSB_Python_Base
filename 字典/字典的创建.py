'''
    字典的创建
    最常用的方法：使用花括号
    sores = {'张三': 100, '李四': 200, '王五': 250}

    使用内置函数dict()
    dict(name = 'sores',age = 20)

'''

'''字典的创建方式'''
'''使用{}创建字典'''
scores = {'张三': 100, '李四': 200, '王五': 250}
print(scores)
print(type(scores))
print(id(scores))

'''使用dict()创建字典'''
students = dict(name = 'students',age = 20)
print(students)
print(type(students))
print(id(students))


'''创建空字典'''
stu = { }
print(stu)
print(type(stu))
print(id(stu))