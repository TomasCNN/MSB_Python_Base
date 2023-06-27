# 列表中的查询操作
'''
    1.获取列表中指定元素的索引
    index()方法
    如查询列表中存在N个相同元素，只返回相同元素中的第一个元素的索引；
    如果查询的元素在列表中不存在，则会抛出ValueError
    还可以在指定的start和stop之间进行查找
    2.获取列表中的单个元素
    正向索引从0到N-1，举例：lst[0]
    逆向索引从-N到-1，举例：lst[-N]
    指定索引不存在，抛出IndexError
'''

list1 = [0,1,2,3,4,1,5,6,7,8]
print(list1.index(1))            # 如查询列表中存在N个相同元素，只返回相同元素中的第一个元素的索引；
# print(list1.index('dashen'))   # 如果查询的元素在列表中不存在，则会抛出ValueError(ValueError: 'dashen' is not in list)
print(list1.index(1,2,6))        # 可以在指定的start和stop之间进行查找

list2 = [0,1,2,3,4,1,5,6,7,8]

# 获取索引为2的元素
print(list2[2])                  # 正向索引从0到N-1，举例：lst[0]

# 获取索引为-3的元素
print(list2[-3])                 # 逆向索引从-N到-1，举例：lst[-N]

# 获取索引为10的元素
#print(list2[10])                # 正向索引从0到N-1，举例：lst[0](IndexError: list index out of range)

'''
    3.获取列表中的多个元素
    语法格式
    列表名[start:stop:step]
    切片的结果->原列表片段的拷贝
    切片的范围->[start:stop]
    step默认为1->简写为[start:stop]
    step为正数->[:stop:step]->切片的第一个元素默认是列表的第一个元素->从start开始往后计算切片
    step为正数->[start::step]->切片的最后一个元素默认是列表的最后一个元素->从start开始往后计算切片
    step为负数->[:stop:step]->切片的第一个元素默认是列表的最后一个元素->从start开始往前计算切片
    step为负数->[start::step]->切片的最后一个元素默认是列表的第一个元素->从start开始往前计算切片

'''

list3 = [0,1,2,3,4,1,5,6,7,8]

# start = 1; step = 1; stop = 6;
print(list3[1:6:1])

# 步长step为正数
print('--------------步长step为正数--------------')
print('原列表：',id(list3))
list4 = list3[1:6:1]
print('切的片段',id(list4))
# start = 1; step默认为1; stop = 6;
print(list3[1:6:])

# start = 1; step = 2; stop = 6;
print(list3[1:6:2])

# start采用默认;step = 2; stop = 6;
print(list3[:6:2])

# start = 1;step = 2; stop采用默认;
print(list3[1::2])

# 步长step为负数
print('--------------步长step为负数--------------')
print('原列表：',id(list3))
# start采用默认;step = -1; stop采用默认;
print(list3[::-1])
# start = 7;step = -1; stop采用默认;
print(list3[7::-1])
# start = 6;step = -2; stop = 0;
print(list3[6:0:-2])

'''
    1.判断指定元素在列表中是否存在
    元素 in 列表名
    元素 not in 列表名
    
    2.列表元素的遍历
    for  迭代变量 in  列表名
        操作
        
'''
print( 'p' in 'pyhton')                                        # True
print( 'k' not in 'pyhton')                                    # True

list = [0,1,2,'hello','world','pythong','Tom']
print( 1 in list)                                              # True
print( 1 not in list)                                          # False
print( 3 in list)                                              # False
print( 3 not in list)                                          # True

print('----------------------------------------------------------------')

for i in list:
    print(i)






