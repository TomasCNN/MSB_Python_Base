'''
    # 列表元素的增加操作

    1.列表元素的增加操作
        append()：在列表的末尾增加一个元素
        extend()：在列表的末尾至少增加一个元素
        insert()：在列表的任意位置增加一个元素
        切片：在列表的任意位置至少增加一个元素
'''

list = [1,2,3,4,7,8,9]
print('添加元素之前：',list,id(list))
list.append(10)
print('添加元素之后：',list,id(list))


list1 = ['python','boy','girl']
list.append(list1)
print('添加列表之后：',list,id(list))
# 将list1作为一个元素添加到列表的末尾
# 输出结果为：添加列表元素之后： [1, 2, 3, 4, 7, 8, 9, 10, ['python', 'boy', 'girl']] 2686778046336

list.extend(list1)
print('添加列表元素之后：',list,id(list))
# 向列表list末尾一次性添加多个元素。
# 输出结果为：添加列表之后： 添加列表元素之后： [1, 2, 3, 4, 7, 8, 9, 10, ['python', 'boy', 'girl'], 'python', 'boy', 'girl'] 2973635999616


# 在列表的任意位置增加一个元素
list.insert(4,5)
print('添加列表元素之后：',list,id(list))


# 在列表中的任意位置上添加N多个元素
list2= [5,6,7,8,9,10]
list[4:] = list2
print('切片之后：',list,id(list))
