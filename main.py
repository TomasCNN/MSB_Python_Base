# Pycharm项目文件结构说明

# ProjectName 项目名
# │ readme 项目说明文档
# │ requirements.txt 存放依赖的外部Python包列表
# │ setup.py 安装、部署、打包的脚本
# ├─ bin 存放脚本，执行文件等
# │ └─ projectname
# ├─ docs 文档和配置
# │ └─ abc.rst
# │ └─ conf.py 配置文件
# └─ projectname 工程源码（包括源码、测试代码等）
# │ main.py 程序入口
# │ init.py
# └─ tests 测试代码
# └─ test_main.py
# └─ init.py

# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
