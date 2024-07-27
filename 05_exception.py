# 异常
# FileNotFoundError
# f = open("D:/abc.tet", "r")
# Traceback (most recent call last):
#   File "D:\python-learn\05_exception.py", line 3, in <module>
#     f = open("D:/abc.tet", "r")
#         ^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'D:/abc.tet'

# 异常处理（捕获异常)---BUG提醒，程序继续运行

# 捕获异常（所有异常）
# try:
#     f = open("D:/abc.tet", "r", encoding="UTF-8")
# except:
#     print("出现异常，w模式打开")
#     f = open("D:/abc.tet", "w", encoding="UTF-8")
#
# try:
#     # 1 / 0
#     # money += 10000
#     print("working")
# except Exception as e:
#     print("出现异常了")
# else:  # 没有异常时执行的代码
#     print("欧耶")


# 捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print(f"name未定义的异常\n{e}")

# 捕获多个异常
# try:
#     # print(1 / 0)
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print("变量未定义或者除数为0")

# finally
# try:
#     f = open("D:/abc.txt", "r", encoding="UTF-8")
# except Exception as e:
#     print("In except")
#     f = open("D:/abc.txt", "w", encoding="UTF-8")
# else:
#     print("No Error")
# finally:
#     print("In finally")
#     f.close()

# 异常的传递性（向上传递）
# def func1():
#     print("beginning of func1")
#     num = 1 / 0
#     print("Ending of func1")
#
#
# def func2():
#     print("beginning of func2")
#     func1()
#     print("Ending of func2")
#
#
# def main():
#     try:
#         func2()
#     except Exception as e:
#         print(f"出现异常了，异常信息为：{e}")
#
#
#
# main()

