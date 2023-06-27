# 列表元素的排列操作

'''
    常见的两种方法
    1.调用sort()方法，列表中所有元素默认按照从小到大得顺序进行排序，
    可以指定reverse = True，进行降序排序；reverse = False  表示升序排序。
    2，调用内置函数sorted（），可以指定reverse = True，进行降序排序，原列表不发生改变，会产生一个新的列表对象。
'''

list = [10,30,54,64,23,45,32,12,17]
print('排序前的列表：','\n',list,'\n',id(list))

# 开始排序，调用列表对象的sort方法，升序排序
list.sort()
print('sort升序排序后的列表：','\n',list,'\n',id(list))
# id显示的结果说明sort方法是在原列表的基础上进行操作的，改变了原列表的元素排列

# 通过指定的关键字参数，将列表中的元素进行降序排序
list.sort(reverse = True)
# reverse = True  表示降序排序；  reverse = False  表示升序排序；
print('sort降序排序后的列表：','\n',list,'\n',id(list))

list.sort(reverse = False)
# reverse = True  表示降序排序；  reverse = False  表示升序排序；
print('sort升序排序后的列表：','\n',list,'\n',id(list))


