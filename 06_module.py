# 使用模块内部的全部功能（类、函数、变量）
# import time
# print("你好")
# time.sleep(1)  # .函数()
# print("我好")
#
# from time import *
# print("你好")
# sleep(1)  # 函数()
# print("我好")

# 使用模块的特定功能（类、函数、变量）
# from time import sleep
# print("你好")
# sleep(1)
# print("我好")

# as 别名
# from time import sleep as tt
# print("你好")
# tt(1)
# print("我好")

# 自定义模块---模块导入重命名会有覆盖现象的出现
# import my_module  # __name__ == "__main__"表示执行本py文件
# from my_module import *  # * 仅仅对应于__all__
# test_A(1, 2)
# # test_B(1, 2)
