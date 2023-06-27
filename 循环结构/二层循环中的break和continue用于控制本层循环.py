# 二层循环中的break和continue用于控制本层循环
'''
    流程控制语句break和continue在二层循环中的使用
'''

for i in range(1,11):                # 行表，执行三次，代表外层循环要执行三次
    for j in range(1,11):            # 列表，执行四次，代表内层循环要执行四次
        if j % 2 == 0:
            break
        print(j)


for i in range(1,11):                # 行表，执行三次，代表外层循环要执行三次
    for j in range(1,11):            # 列表，执行四次，代表内层循环要执行四次
        if j % 2 == 0:
            continue
        print(j,end = '\t')
    print()