# 条件表达式
# 条件表达式是if……else的简写
# 语法结构
'''
    x if 判断条件 else y
'''

# 运算规则
'''
    如果判断条件的布尔值为True,条件表达式的返回值x，否则条件表达式的返回值为False.
'''

# 从键盘录入两个整数，比较两个整数的大小
num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))

# 比较大小

if num_a >= num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)

# 使用条件表达式进行比较
print('使用条件表达式进行比较')
print((str(num_a) + ' 大于等于 ' + str(num_b))  if num_a >= num_b  else  (str(num_a) + ' 小于 ' + str(num_b)))