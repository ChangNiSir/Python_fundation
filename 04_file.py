# 文件编码---UTF-8（世界通用编码）
# GBK---简体中文
# Big5---繁体中文

# 文件的操作
# 打开文件
# "w"---原有内容会被删除
# "a"---追加内容
# f = open("D:/云计算/input.txt", "r", encoding="UTF-8")  # 使用斜杠

# 读写文件---f会移动
# read()---默认读取全部内容（返回字符串）
# f = open("D:/云计算/input.txt", "r", encoding="UTF-8")  # 使用斜杠
# print(f"读取10个字节的结果为：{f.read(1)}")
# print(f"读取全部内容的结果为：\n{f.read()}")  # 读取剩余全部内容

# readlines()---读取全部行封装到列表中
# f = open("D:/云计算/input.txt", "r", encoding="UTF-8")  # 使用斜杠
# print(f"读取全部行进行封装后得到：{f.readlines()}")

# readline()
# f = open("D:/云计算/input.txt", "r", encoding="UTF-8")  # 使用斜杠
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据为：{line1}")
# print(f"第二行数据为：{line2}")
# print(f"第三行数据为：{line3}")

# for循环
# f = open("D:/云计算/input.txt", "r", encoding="UTF-8")  # 使用斜杠
# for line in f:
#     print(f"每一行内容：{line}")
# # .close()---关闭文件
# f.close()

# with open()方法自动close文件
# with open("D:/云计算/input.txt", "r", encoding="UTF-8") as f:
#     print(f.readlines())

# print("===========================================")
# f = open("D:/word.txt", "r", encoding="UTF-8")

# 方法1
# count_apple = 0
# for line in f:  # 这里遍历f即可
#     # print(type(line))
#     count_apple += line.count("apple")
# print(f"word.txt中出现了{count_apple}次苹果")
# f.close()

# 方法2
# content = f.read()
# count_apple = content.count("apple")
# print(f"word.txt中出现了{count_apple}次苹果")
# f.close()

# 方法3
# count_apple = 0
# for line in f:
#     line = line.strip("\n")
#     words = line.split(" ")  # 1 返回列表 2 会有apple\n的情况
#     # print(words)
#     for word in words:
#         if word == "apple":
#             count_apple += 1
# print(f"word.txt中出现了{count_apple}次苹果")
# f.close()

# 写文件
# 内容刷新
# f.write()  # 写入内存
# f.flush()  # 刷新内容到硬盘中（攒一堆，一次性写入硬盘）

# f = open("D:/test.txt", "w", encoding="UTF-8")  # 文件不存在创建新文件
# f.write("Hello World")
# # f.flush()
# f.close()  # 内置.flush()

# f = open("D:/test.txt", "w", encoding="UTF-8")  # 1 文件不存在创建新文件 2 清空内容写
# f.write("apple banana")
# f.close()

# 追加模式 "a"---需要.flush()（.close()内置）
# f = open("D:/test.txt", "a", encoding="UTF-8")  # 文件不存在创建新文件
# f.write("Hello World!!!")
# f.write("\nThis is an apple.")
# f.close()

# print("================================")
# f_r = open("D:/bill.txt", "r", encoding="UTF-8")
# f_bak = open("D:/bill.txt.bak", "a", encoding="UTF-8")
# for line in f_r:
#     if line.strip("\n").split(",")[-1] == "测试":
#         continue
#     # else:
#     #     f_bak.write(line)
#     f_bak.write(line)
# f_r.close()
# f_bak.close()


