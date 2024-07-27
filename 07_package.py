# Python包（文件夹）
# 一堆Python模块 + _init_.py文件

# 导入具体模块
#
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()
#
# from my_package import my_module1
# from my_package import my_module2
#
# my_module1.info_print1()
# my_module2.info_print2()

# 导入具体功能
#
# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
#
# info_print1()
# info_print2()

# 导入包的全部功能
#
# from my_package import *
#
# my_module1.info_print1()
# # my_module2.info_print2()
#
# from my_package import my_module1, my_module2
#
# my_module1.info_print1()
# my_module2.info_print2()

# print("========================================")
#
# import my_utils.str_util
# from my_utils import file_util
#
# str_reverse = my_utils.str_util.str_reverse("abcdefg")
# str_2_5 = my_utils.str_util.substr("123456", 2, 5)
# print(f"abcdefg字符串反转得到：{str_reverse}")
# print(f"12345第2个元素到第5个元素为：{str_2_5}")
#
# file_name = "D:/word.txt"
# data = "\nlike you apple and banana"
# file_util.print_file_info(file_name)
# file_util.append_to_file(file_name, data)

# 注意：需要在__init__.py中配置__all__列表才能 1 import my_utils as mu  2 mu.str_util.str_reverse("123456")
# from my_utils import *  # 导入__all__配置的包（初始为空）
# str_util.str_reverse()


# 第三方包的安装
# 安装位置（D:\dev\python\python3.12.4\Lib\site-packages）
# pip install numpy
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
