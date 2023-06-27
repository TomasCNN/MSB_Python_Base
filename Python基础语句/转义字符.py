# Python转义字符

# 什么是转义字符？
# 反斜杠 + 想要实现的转义字符功能的首字母

#为什么需要转义字符？
# 档子附中包含反斜杠、单引号或双引号等有特殊用途的字符时，必须使用反斜杠这类转义字符进行转义（转换一个含义）
# 反斜杠： \\       单引号：\'       双引号：\"
# 当字符串中包含换行、回车、水平制表符或退格等无法直接表示的特殊字符时，也可以使用转义字符
# 换行：\n         回车：\r       水平制表符：\t        退格：\b

# 转义字符	描述
# \ （在行尾时）	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \0 / \000	空字符(NULL)
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数 yy 代表的字符，例如， \o12 代表换行
# \xyy	十六进制数 yy 代表的字符，例如， \x0a 代表换行
# \other	其他字符以普通格式输出
# \ddd	1到3位八进制数所代表的的任意字符
# \n	换行符，将光标位置移到下一行开头。
# \r	回车符，将光标位置移到本行开头。
# \t	水平制表符，也即 Tab 键，一般相当于四个空格。
# \a	蜂鸣器响铃。注意不是喇叭发声，现在的计算机很多都不带蜂鸣器了，所以响铃不一定有效。
# \b	退格（Backspace），将光标位置移到前一列。
# \\	反斜线
# \'	单引号
# \"	双引号
# \	在字符串行尾的续行符，即一行未完，转到下一行继续写。

# 转义字符
# \ + 转义功能的首字母

# n:newline的首字母表示换行
print('hello\nworld')

# \t制表位，4格
# hell-o   -worl-d
# hell-oooo-    -worl-d

print('hello\tworld')
print('helloooo\tworld')

# \r光标退到行首
print('hello\rworld')

# \b光标退一个格
print('hello\bworld')
print('老师说:\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，就用转义字符，就是在字符串之间加上r或者R
print(r'hello\nworld')
#PS:最后一个字符不能是反斜杠
#print(r'hello\nworld\')


print(r'hello\nworld\\')
print('Hello World!')
print('Hello\nWorld!')
print('Hello\rWorld!')
print('Hello\tWorld!')
print('Hellooo\tWorld!')
print('Hello\bWorld!')
print('Hello\rWorld!')
print('Hello\rWorld!')


