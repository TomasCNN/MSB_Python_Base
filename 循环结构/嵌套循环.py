# 嵌套循环
# 循环结构中又嵌套了另外的完整的循环结构，其中内层循环作为外层循环的循环体执行


'''
    输出一个三行四列的矩形
'''

for i in range(1,4):                # 行表，执行三次，一次是一行
    for j in range(1,5):            # 列表，执行四次，一次是一列
        print('*',end = '\t')       # 不换行输出
    print()

# 外层循环控制的是打印的行数，内层循环控制的是打印的个数


'''
    输出一个直角三角形
'''

for i in range(1,10):                # 行表，执行三次，一次是一行
    for j in range(1,10):            # 列表，执行四次，一次是一列
        if i >= j:
            print('*',end = '\t')    # 不换行输出
        else:
            continue
    print()

'''
    输出一个直角三角形
'''

for i in range(1,10):                # 行表，执行三次，一次是一行
    for j in range(1,i + 1):         # 列表，执行四次，一次是一列
        print('*',end = '\t')        # 不换行输出
    print()

'''
    输出一个九九乘法表
'''

for i in range(1,10):                # 行表，执行三次，一次是一行
    for j in range(1,i + 1):         # 列表，执行四次，一次是一列
        print(i,'*',j,'=',i * j,end = '\t')        # 不换行输出
    print()