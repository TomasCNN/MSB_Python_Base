'''
    # 列表元素的删除操作
    remmove():
        一次删除一个元素
        重复元素只删除第一个
        元素不存在抛出ValueError
    pop():
        删除一个指定索引位置上的元素
        指定索引不存在抛出ValueError
        不指定索引，删除列表中最后一个元素
    切片：一次至少删除一个元素
    clear():清空列表
    del：删除列表
'''

list = [10,20,30,40,50,60,30]

# 从列表中一次只删除一个元素
list.remove(40)
print('删除40后的列表：',list)

# 从列表中一次只删除一个元素，如果有重复的元素就删除重复元素中的第一个元素
list.remove(30)
print('删除30后的列表：',list)

# 需要删除的元素不存在列表中时，抛出ValueError（ValueError: list.remove(x): x not in list）
# list.remove(1100)

# pop（）根据索引删除元素
list.pop(1)
print('删除索引为1的元素后的列表：',list)

# 指定索引不存在列表中时，抛出ValueError(IndexError: pop index out of range)
# list.pop(10)

# 如果不指定索引，将删除列表中最后一个元素
list.pop()
print('删除不指定索引元素后的列表：',list)

print('--------------------------切片操作，删除至少一个元素，将产生一个新的列表对象--------------------------')
list1 = [1,2,3,4,5,6,7,8,9,10]
temp_list = list1[1:5]
print('原列表：',list1)
print('切片后的新列表：',temp_list)

print('--------------------------切片操作，不产生新的列表对象，，而是删除原列表中的内容--------------------------')
list1[1:5] = []
print('不产生新列表切片后的新列表：',list1)

# 清除列表中的所有元素
list1.clear()
print('清除了列表中所有元素后的新列表：',list1)

# 删除列表对象
# 报错信息：NameError: name 'list1' is not defined. Did you mean: 'list'?
del list1
# print('删除列表后的列表输出：',list1)