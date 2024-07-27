# list
# my_list = ['python', 666, True, 666, 'a', 666, [1, 2, 3]]  # -4 -3 -2 -1 / 0  1  2  3
# print(my_list)
# print(my_list[-1])  # 下标索引
# print(my_list[-1][1])
# print(my_list[0][1])

# 列表的常用操作
# .index
# index = my_list.index([1, 2, 3])
# print(f"index = {index}")
#
# index = my_list.index([1, 2])
# print(f"index = {index}")
#
# 修改指定位置元素
# print(my_list)
# my_list[0] = "hello"
# print(my_list)
#
# # .insert()---指定位置插入元素
# my_list.insert(0, "first")
# print(my_list)
#
# # .append()---尾部追加单一元素
# my_list.append("last")
# print(my_list)
#
# # .extend(数据容器)---追加批量元素
# my_list.extend([1, 2, 3])
# print(my_list)
#
# 删除指定位置元素
# del
# del my_list[-4]  # 删除last
# print(my_list)
#
# .pop()---删除元素并返回
# elem = my_list.pop(-4)
# print(elem, my_list)
#
# 删除指定内容元素
# .remove()---从前到后的第一个元素
# my_list.remove("last")
# print(my_list)
#
# .clear()---清空列表
# my_list.clear()
# print(my_list)
#
# len(列表) / .count()
# print(f"列表长度为：{len(my_list)}，666的个数为：{my_list.count(666)}")

# 应用
# mylist = [21, 25, 21, 23, 22, 20]
# print(mylist)
# mylist.append(31)
# print(mylist)
#
# mylist.extend([29, 33, 30])
# print(mylist)
#
# num1 = mylist[0]
# print(num1)
#
# num2 = mylist[-1]
# print(num2)
#
# print(mylist)
# index = mylist.index(31)
# print(index)

# 列表的遍历
# while
# def list_while_func():
#     mylist = [21, 25, 21, 23, 22, 20]
#     index = 0  # 下标
#     while index < len(mylist):  # i <= len(mylist) - 1
#         element = mylist[index]
#         print(element, end=" ")
#         index += 1
#
#
# list_while_func()


# for
# def list_for_func():
#     mylist = [21, 25, 21, 23, 22, 20]
#     for element in mylist:
#         print(element, end=" ")
#
#
# list_for_func()

# 取偶数
# for
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_list = []
# for element in mylist:
#     if element % 2 == 0:
#         even_list.append(element)
# print(even_list)

# while
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_list = []
# index = 0
# while index < len(mylist):  # 循环控制条件
#     element = mylist[index]
#     if element % 2 == 0:
#         even_list.append(element)
#     index += 1  # 循环变量改变防止死循环
# print(even_list)

# tuple---一旦定义不能篡改（只读不写）
# my_tuple = (1, "hello", True, (1, 2, 3), "hello", "hello")
# # t1 = ("hello", )
# print(type(my_tuple), "---", my_tuple)
# print(my_tuple[-1][-1])
#
# # .index()
# index = my_tuple.index("hello")  # 这里 1 == True
# print(index)
#
# # .count() / len(my_tuple)
# count = my_tuple.count("hello")
# print(f"hello字符串个数有{count}个，共有{len(my_tuple)}个")

# 元组遍历
# my_tuple = (1, "hello", True, (1, 2, 3), "hello", "hello")
# while循环
# index = 0
# while index < len(my_tuple):
#     print(my_tuple[index])
#     index += 1

# for循环
# my_tuple = (1, "hello", True, (1, 2, 3), "hello", "hello")
# for element in my_tuple:
#     print(f"元组的元素有：{element}")


# print("==============================================")
# my_tuple = ("周杰伦", 11, ["football", "music"])
# index = my_tuple.index(11)
# name = my_tuple[0]
# del my_tuple[2][0]
# my_tuple[2].append("coding")
# print(f"年龄下标{index}，姓名{name}，新的元组为：{my_tuple}")


# 字符串---只读不可修改（增加、删除、内容修改）
# my_str = "nian nian bu wang, bi you hui xiang"
# value = my_str[-16]
# print(f"下表-16字符值为{value}")
# print(my_str.index('bu'))

# .replace(str1, str2)---str1替换为str2->有返回值（新的字符串对象）
# my_str = "nian nian bu wang, bi you hui xiang"
# new_my_str = my_str.replace("wang", "zou")
# print(f"my_str为：{my_str}\nnew_my_str为：{new_my_str}")

# .split("分割字符")---字符串分割->列表对象
# my_str = " I do this for you "
# my_str_list = my_str.split(" ")
# print(f"{my_str}按空格分割后得到{my_str_list}，其类型为{type(my_str_list)}")

# .strip("去除的字符串前后所删字符(可以随机组合多个字符)")---字符串规整操作（针对空格回车及字符）
# my_str = " 12I do this for you21 "
# print(my_str)
# print(my_str.strip())
# print()
# print(my_str.strip("12 "))
# print(my_str.strip("21 "))
# print(my_str.strip("1 2 "))
# print(my_str.strip(" 21"))
# print(my_str.strip(" 12 "))

# print("======================")
# my_str = "itheima and itcast"
# count = my_str.count("it")
# print(f"{my_str}中有{count}个\"it\"")
# new_my_str = my_str.replace(" ", "|")
# print(f"{my_str}修改后得到{new_my_str}")
# new_my_str_list = new_my_str.split("|")
# print(f"分割后得到{new_my_str_list}")


# 序列切片（不含结束下标）
# my_list = [0, 1, 2, 3, 4, 5, 6]
# result = my_list[::-2]
# result = my_list[::-2]
# result = my_list[3:1:-1] # 负数step始末要颠倒
# result = my_list[::-1]  # -1 表示逆序步长，表示倒序执行
# # result = my_list[1:4]  # 不含结束下标4
# print(result)

# print("================================")
# my_str = "你想好我，施西"
# new_str = my_str[3:0:-1]  # 0写了才不包含0，0不写的话就会直接输出到开头
# print(new_str)


# 集合（允许修改）---去重但无序（不支持下表索引访问）
# my_set = {"Hello", "hello", "Hello", "Xtuer"}
# my_set_empty = set()
# print(f"my_set内容为{my_set}")
#
# my_set.add("python")
# print(f"my_set添加元素后{my_set}")
#
# my_set.remove("Hello")
# print(f"my_set移除元素后{my_set}")
#
# element = my_set.pop()
# print(f"my_set随机取出元素{element}后得到{my_set}")

# my_set.clear()  # 无返回值（None）

# # 集合运算
# set1 = {1, 2, 3}
# set2 = {1, 5, 6}
# # 差集
# set1.difference_update(set2)  # set3 = set1.difference(set2)
# print(f"set1有而set2没有的是{set1}")  # print(f"{set1}有而{set2}没有的是{set1}")
#
# # 并
# set4 = set1.union(set2)
# print(f"set1并set2得到{set4}，集合元素个数为：{len(set4)}")

# 遍历只能for循环，无序不支持下标索引（while不行）

# print("=============================================")
# my_list = ["I", "like", "banana", "juice", "banana", "juice"]
# my_set_empty = set()
# for element in my_list:
#     my_set_empty.add(element)
# print(f"{my_list}添加到my_set_empty得到：\n{my_set_empty}")


# 字典（不允许key重复否则会更新内容）---key:value
# 定义---key不为字典
# my_dict_empty = dict()  # {}
# print(f"my_dict_empty的结果：{my_dict_empty}")  # 输出：{}  # 集合不能用{}定义的原因
# my_dict = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
# print(f"my_dict内容为：{my_dict}，类型为：{type(my_dict_empty)}")
# score = my_dict["周杰伦"]
# print(f"周杰伦的分数为{score}")

# 字典的嵌套
#   学生姓名      学生信息
#             学科    成绩
#
# stu_score_dict = {
#     "王力宏": {
#         "语文": 77,
#         "数学": 66,
#         "英语": 33
#     }, "周杰伦": {
#         "语文": 88,
#         "数学": 86,
#         "英语": 55
#     }, "林俊杰": {
#         "语文": 99,
#         "数学": 96,
#         "英语": 66
#     }
# }
# print(f"score_dict为{stu_score_dict}")
#
# # 获取数据
# score = stu_score_dict["周杰伦"]["语文"]
# print(f"周杰伦的语文成绩为：{score}")

# 字典常用操作
# my_dict = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}

# 获得所有keys
# keys = my_dict.keys()
# print(f"字典的全部Key为：{keys}")
#
# # 增加
# my_dict["张信哲"] = 66
# print(f"新增元素后{my_dict}")
#
# # 更新
# my_dict["周杰伦"] = 33
# print(f"更新元素后{my_dict}")
#
# # 删除
# value = my_dict.pop("周杰伦")
# print(f"删除元素值为：{value}，字典改为：{my_dict}")

# 遍历
# 方式1
# print(f"字典长度为{len(my_dict)}")
# for key in my_dict.keys():
#     print(f"字典元素{key}对应{my_dict[key]}")

# len()
# print(f"字典长度为{len(my_dict)}")

# # 方式2
# for key in my_dict:
#     print(f"字典元素{key}对应{my_dict[key]}")

# 字典不支持下标索引---No for

# 清空元素
# my_dict.clear()
# print(f"清空元素后{my_dict}")

# print("==================================")
# staff_dict = {
#     "王力宏": {
#         "部门": "科技部",
#         "工资": 3000,
#         "级别": 1
#     },
#     "周杰伦": {
#         "部门": "市场部",
#         "工资": 5000,
#         "级别": 2
#     },
#     "林俊杰": {
#         "部门": "市场部",
#         "工资": 7000,
#         "级别": 3
#     },
#     "张学友": {
#         "部门": "科技部",
#         "工资": 4000,
#         "级别": 1
#     },
#     "刘德华": {
#         "部门": "市场部",
#         "工资": 6000,
#         "级别": 2
#     }
# }
#
# print(f"修改前的字典为：{staff_dict}")
# for key in staff_dict:
#     # 获取员工信息（视图？）
#     info_dict = staff_dict[key]
#     if info_dict["级别"] == 1:
#         info_dict["级别"] = 2
#         info_dict["工资"] += 1000
#     # print(key, staff_dict[key])
#     # 更新回staff_dict[key]
#     staff_dict[key] = info_dict
# print(f"员工级别1的级别加1，增加1000工资\n修改后的字典为：{staff_dict}")

# 数据容器的操作
# 遍历

# len()

# max() / min()
# my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
# print(f"字典中最大为{max(my_dict)}，字典中最小为{min(my_dict)}")

# list() / str() / tuple() / set()

# sorted(容器, [reverse=False])---返回列表对象
# my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
# print(sorted(my_dict))

