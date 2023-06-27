# 比较运算符

# 对变量或表达式的结果进行大小、真假等比较

a,b = 10,20
print('a > b ?',a > b)
print('a < b ?',a < b)
print('a == b ?',a == b)
print('a >= b ?',a >= b)
print('a <= b ?',a <= b)
print('a != b ?',a != b)

'''
一个 "=" 称为复制运算符;
一个 "==" 称为比较运算符
一个变量由三部分组成:标识、类型、值.whnfkljasedhsndgkjads
"=="比较的是值
比较对象的1标识使用  is

'''

a = 10
b = 10
print(a == b)   # True   a与b的值(value)相等
print(a is b)   # True   a与b的ID(标识)相等
print("a的值:",a,"\n","a的ID:",id(a),"\n","a的类型:",type(a),"\n")
print("b的值:",b,"\n","b的ID:",id(b),"\n","b的类型:",type(b),"\n")

lst1 = [11,22,33,44,55,66]
lst2 = [11,22,33,44,55,66]
print(lst1 == lst2)
print(lst1 is lst2)
print(a is not b)
print(lst1 is not lst2)