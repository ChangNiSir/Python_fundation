"""
程序：python_fd.py
类
方法
"""
# 建议要求（规范）
# print("666" + "字符串")

# 变量
# money = 100.50
# print("钱包还有：", money)
#
# money -= 10
# print("钱包还有：", money, "￥")

# 数据类型
# float_type = type(money)
# print(float_type)


# 类型转换
# num_str = str(123)
# print(type(num_str), num_str)
#
# str_num = int("123")  # 数字类型字符串才可转换为数字
# print(type(str_num), num_str)
#
# num_float = float(123)
# print(type(num_float), num_float)
#
# float_int = int(11.345)  # 精度丢失
# print(type(float_int), float_int)


# 标识符---数字不开头
# 变量---全小写下划线
# name_other_1 = "静静"
# 类
# 方法


# 算数运算符
# print("1 + 1 = ", 1 + 1)
# print("2 - 1 = ", 2 - 1)
# print("3 * 3 = ", 3 * 3)
# print("4 / 2 = ", 4 / 2)
# print("11 // 3 = ", 11 // 3)
# print("9 % 2 = ", 9 % 2)
# print("2 ** 2 = ", 2 ** 2)

# 赋值运算符 = -= += *= /= %= **= //=
# num = 1
# num += 1
# print(num)


# 字符串
# 定义
# poem = """
# 你好
# 就是好
# """
# print(poem)
# print('"黑马"')
# print("'黑马'")
# print('\'黑马\'')
# print("\"黑马\"")

# 拼接--- %s %d %f占位格式化
# name = "**程序员"
# class_num = 57  # 整数可以转换为字符串也可占位输出
# print("你好，" + name)
# message = "学IT来%s，有%s名的学员。" % (name, class_num)
# print(message)

# 占位格式化 + 精度控制
# name = "**视频"
# setup_year = 2006
# stock_price = 19.99  # 宽度包括小数点，后面小数精度四舍五入
# message = "%s成立于%5d年，股价%6.2f" % (name, setup_year, stock_price)
# print(message)

# 快速格式化format---不限数据类型，不做精度控制
# print(f"{name}成立于：{setup_year}年，股价：{stock_price}")

# 表达式格式化---不存储数据时  print(f"-----{1 * 1}")
#                         print("-----%d" %(1 * 1))
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# final_stock_price = stock_price*stock_price_daily_growth_factor**growth_days
# print(f"{name}的股票代码：{stock_code}，当前股价：{stock_price}")
# print("每日增长系数：%.1f，经过了%d天的增长，当前股票价格：%.2f" % (stock_price_daily_growth_factor, growth_days, final_stock_price))


# 数据输入
# name = input("\n请告诉我Who are you?")
# print("Hello, I am %s" % name)

# num = int(input("\n请输入密码："))  # input("\n请输入密码：")
# print("密码类型：%s" % type(num))

# user_name = input("\n请输入姓名：")
# user_type = input("请输入会员等级：")
# print("%s，你好，您是尊贵的%s，欢迎登录！" % (user_name, user_type))

# 逻辑判断
# result = "abc" < "abd"  # 字符串可以使用 == <= ...
# print(result, type(result))

# if语句
# age = int(input("\n欢迎来到游乐场，儿童免费，成人收费\n请输入您的年龄："))
# if age >= 18:
#     print("您已成年，游玩需要补票10元。")
# else:
#     print("您未成年，免费游玩。")
# print("祝您玩的愉快")

# height = int(input("\n请输入你的身高（cm）："))
# vip_level = int(input("请输入你的VIP级别（1~5）:"))
# day = int(input("请告诉我今天几号："))
# if int(input("\n请输入你的身高（cm）：")) < 120:
#     print("您的身高小于120cm，免费游玩。")
# elif int(input("请输入你的VIP级别（1~5）:")) > 3:  # elif等同于的else if
#     print("您的VIP等级大于3，可以免费游玩。")
# elif int(input("请告诉我今天几号：")) == 1:
#     print("今天是1号，可以享有优惠。")
# else:
#     print("不好意思，您无法享有优惠，需要加价10元。")
# print("祝您玩的愉快！！！")

# 下述内容仅联系语法，实际循环更得当

# num = 5
# if int(input("请输入第一次猜想的数字：")) == num:
#     print("猜对了")
# elif int(input("不对再猜一次：")) == num:
#     print("猜对了")
# elif int(input("不对再猜最后一次：")) == num:
#     print("猜对了")
# else:
#     print("猜错了")

# 嵌套if注意每一层先完善再嵌套
# think_num = 6
# talk_num = int(input("请输入第一次猜想的数字："))
# if talk_num != think_num:
#     talk_num = int(input("不对再猜一次："))
#     if talk_num != think_num:
#         talk_num = int(input("不对再猜最后一次："))
#         if talk_num != think_num:
#             print("我心里想的是%d" % think_num)
#         else:
#             print("猜对了")
#     else:
#         print("猜对了")
# else:
#     print("猜对了")

# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制")
#     if int(input("你的VIP级别是多少：")) > 3:
#         print("可以免费")
#     else:
#         print("不免费")
# else:
#     print("免费")

# age = 25
# work_year = 5
# work_level = 1
# if age >= 18:
#     print("you are an adult")
#     if age < 30:
#         print("age is OK")
#         if work_year > 2:
#             print("work_year is OK, gift to you")
#         elif work_level > 3:
#             print("work_level is OK, gift to you")
#         else:
#             print("sorry，work_year and work_level are not up to standard")
#     else:
#         print("sorry, age is big")
# else:
#     print("sorry，age is small")

# import random
# num = random.randint(1, 10)
# guess_num = int(input("第一次猜数："))
# if guess_num > num:
#     print("猜大了")
#     guess_num = int(input("第二次猜数："))
#     if guess_num > num:
#         print("猜大了")
#         guess_num = int(input("第三次猜数："))
#         if guess_num > num:
#             print("猜大了，游戏结束")
#         elif guess_num < num:
#             print("猜小了，游戏结束")
#         else:
#             print("猜对了，num = %d" % num)
#     elif guess_num < num:
#         print("猜小了")
#         guess_num = int(input("第三次猜数："))
#         if guess_num > num:
#             print("猜大了，游戏结束")
#         elif guess_num < num:
#             print("猜小了，游戏结束")
#         else:
#             print("猜对了，num = %d" % num)
#     else:
#         print("猜对了，num = %d" % num)
# elif guess_num < num:
#     print("猜小了")
#     guess_num = int(input("第二次猜数："))
#     if guess_num > num:
#         print("猜大了")
#         guess_num = int(input("第三次猜数："))
#         if guess_num > num:
#             print("猜大了，游戏结束")
#         elif guess_num < num:
#             print("猜小了，游戏结束")
#         else:
#             print("猜对了，num = %d" % num)
#     elif guess_num < num:
#         print("猜小了")
#         guess_num = int(input("第三次猜数："))
#         if guess_num > num:
#             print("猜大了，游戏结束")
#         elif guess_num < num:
#             print("猜小了，游戏结束")
#         else:
#             print("猜对了，num = %d" % num)
#     else:
#         print("猜对了，num = %d" % num)
# else:
#     print("猜对了，num = %d" % num)

# 代码优化---还可循环优化
# import random
# num = random.randint(1, 10)
# guess_num = int(input("第一次猜数："))
# if guess_num == num:
#     print("猜对了，num = %d" % num)
# else:
#     if guess_num > num:
#         print("猜大了")
#     else:
#         print("猜小了")
#     guess_num = int(input("第二次猜数："))
#     if guess_num == num:
#         print("猜对了，num = %d" % num)
#     else:
#         if guess_num > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#         guess_num = int(input("第三次猜数："))
#         if guess_num == num:
#             print("猜对了，num = %d" % num)
#         else:
#             if guess_num > num:
#                 print("猜大了，游戏结束")
#             else:
#                 print("猜小了，游戏结束")


# 循环
# while循环
# num_sum = 0
# i = 1
# while i <= 100:
#     num_sum += i
#     i += 1
# print("1 + 2 + ... + 100 = %d" % num_sum)

import random
num = random.randint(1, 100)
count = 0  # 记录猜测次数
flag = True  # 循环终止变量
while flag:
    guess_num = int(input("请猜出数字："))
    count += 1
    if guess_num == num:
        print("猜对了%d，猜了%d次" % (num, count))
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")
    # python不常用一下写法
    # if guess_num > num:
    #     print("猜大了")
    # elif guess_num < num:
    #     print("猜小了")
    # else:
    #     print("猜对了%d，猜了%d次" % (num, count))
    #     flag = False  # break

























