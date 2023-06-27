# print（）函数
# 作用：作出相应的执行，在屏幕上输出相应的结果。
# print（）函数输出的内容可以是：数字、字符串、含有运算符的表达式
# print（）函数可以将内容输出到：显示器（屏幕）或文件中、
# print（）函数可以换行输出也可以不换行输出。

print('Hello,World!')
print(531)
print(565+98)
print(987*654)
print(3**3)

# 将数据输出到文件中，注意点：1.所指定的文件（盘符地址）位置要存在；2.要使用"file=FileName";说明文件名
FileName = open('text.txt', 'a+')    # "a+":表示的是如果这个文件不存在就创建这个文件；如果这个文件存在就在这个文件的现有内容后继续换行追加内容。
print("Hello,Python,I'm Coming!",file = FileName)
FileName.close()


