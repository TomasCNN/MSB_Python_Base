# range()函数
'''
    1.用于生成整数序列；
    2.创建range对象的三种方式；
        a.range(stop) : 创建一个[0，stop]之间的整数序列，步长为1；
        b.range(start，stop)  : 创建一个[start，stop]之间的整数序列，步长为1；
        c.range(start，stop,step)  : 创建一个[start，stop]之间的整数序列，步长为step;
    3.返回值是一个迭代器对象；
    4.range类型的优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，因为仅仅需要存储
        start，stop和step，只有当用到range对象时，才会去计算序列中的相关元素
    5.in与not in判断整数序列中是否存在1（不存在）指定的整数
'''

# range()的三种使用方式
'''第一种创建方式，只有一个参数（小括号中只给了一个数）'''
range1 = range(10)          # [0,1,2,3,4,5,6,7,8,9]  默认从0开始，步长为1；
print(range1)               # range(0,10)
print(list(range1))         # 用于查看range对象中的整数序列    --> list是列表的意思


'''第二种创建方式，给了两个参数（小括号中给了两个数）'''
range2 = range(1,10)        # 指定了起始值，从1开始，到10结束（不包含10）
print(list(range2))         # [1,2,3,4,5,6,7,8,9]


'''第三种创建方式，给了三个参数（小括号中给了三个数）'''
range3 = range(1,10,2)      # 指定了起始值，从1开始，到10结束（不包含10）
print(list(range3))         # [1,3,5,7,9]


'''第三种创建方式，给了三个参数（小括号中给了三个数）'''
print(10 in range3)         # False,10不在当前的range3这个整数序列中
print(9 in range3)          # True,9不在当前的range3这个整数序列中

print(10 not in range3)     # True,10不在当前的range3这个整数序列中
print(9 not in range3)      # False,9不在当前的range3这个整数序列中

print(range(1,20,1))        # [1,…………,19]
print(range(1,101,1))       # [1,…………,100]