# 标识符与保留字

# 标识符就是程序中，使用的各种名称，例如：变量名、常量名、类名等等。
# 在 Python 中，对标识符格式的要求与 C/C++、Java等差不多：

# 1.第一个字符必须是字母表中的字母或下划线 _ ；
# 2.标识符的其他的部分，由字母、数字和下划线组成；
# 3.标识符对大小写敏感；
# 4.标识符不能与保留字（关键词）相同。

# 保留字即关键字，是 Python 语言中内部使用的单词，代表一定语义。
# 例如：and、class、if、else等。
#
# 保留字不能作为标识符，用在变量名、常量名、类名等地方。
# Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：


import keyword
print(keyword.kwlist)

# 保留字有：
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', \
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', \
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', \
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']