# Pass语句
# 语句什么都不用做，只是一个占位符，用在语法上需要语句的地方
# 什么时候用？先搭建与语法结构，还没想好代码怎么写的时候。
# 哪些语句一起使用？
'''
    if 语句的条件执行体
    for - in 语句的循环体
    定义函数时的函数体
'''

# Pass 语句
# 语法结构
'''
    pass语句什么都不用做，只是一个占位符，用在语法上需要语句的地方
'''

'''
    会员  
            ……
    非会员
            ……
'''

answer = input('您是会员吗？Y/N：')
cost = float(input('请输入您对购物金额（元）：'))

# 条件判断
if answer == 'Y':                 # 会员
    pass
else:                             # 非会员
    pass