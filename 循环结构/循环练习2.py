'''
    输出100-999之间的水仙花数
    举例：
    153 = 3*3*3 + 5*5*5 + 1*1*1
'''
for i in range(100,1000):
    a = i % 10        # 个位数字
    b = i // 10 % 10  # 十位数字
    c = i // 100      # 百位数字
    # print(a,b,c)
    # 判断
    if a**3 + b**3 + c**3 == i:
        print(i)