'''
    # 列表生成式
    # 简称生成列表的公式
    # 语法格式：
    [i*i  for i in range(1,10)]
    "i*i"：表示列表元素的表达式；
    "i":自定义变量；
    “range(1,10)”：可迭代对象
    注意事项：“表示列表元素的表达式”中通常包含自定义变量
'''

list = [ i for i in range(1,10)]
print(list)

'''列表中的元素值为2,4,6,8,10'''
list2 = [ i*2 for i in range(1,6)]
print(list2)

