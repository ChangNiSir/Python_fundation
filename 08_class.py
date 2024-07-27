# 设计类
# self表示对象本身
# self必须写入传参列表中
# 成员方法中访问成员变量使用self

# class Student:
#     name = None
#     age = None
#     gender = None
#
#     # 构造方法 __init__()
#     def __init__(self, name, age, gender):  # 使用提示回车注意是否为__init__
#         # 成员变量的定义和赋值
#         self.name = name
#         self.age = age
#         self.gender = gender
#         print("对象创建成功!")
#
#     def say_hi1(self):
#         print(f"大家好，我是{self.name}，年龄：{self.age}，性别：{self.gender}")
#
#     def say_hi2(self, msg):
#         print(f"大家好，我是{self.name}，{msg}")
#
#
# stu = Student("周杰伦", 31, "男")
# stu.say_hi1()


# class Student:
#
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def __str__(self):  # 重写object中的方法
#         return f"Student类对象：name={self.name}，age={self.age}，address={self.address}"
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
#     def __eq__(self, other):  # 重写object中的方法
#         return self.age == other.age


# 字典value值为对象
# student = {}
# for index in range(2):
#     print(f"当前录入第{index + 1}位学生信息，总共需要录入10位学生信息")
#     name = input("请输入学生姓名：")
#     age = input("请输入学生年龄：")
#     address = input("请输入学生地址：")
#     student[index] = Student(name, age, address)
#     print(f"学生{index + 1}信息录入完成，信息为：【学生姓名：{student[index].name}，年龄：{student[index].age}，地址：{student[index].address}】")
#
# print(type(student))

# 魔术方法
# stu = Student("周杰伦", 31, "台湾")
# stu1 = Student("周杰伦", 32, "台湾")
#
# __str__字符串方法----->控制类转化为字符串
# print(stu)  # 魔术方法可以简化使用
# print(str(stu))  # 类似方法重写
#
# __lt__ / __le__ / __eq__ ----->对象进行比较
# __lt__
# print(stu < stu1)
# print(stu > stu1)
#
# __le__
# print(stu <= stu1)
# print(stu >= stu1)
#
# __eq__  # 未实现时比较对象的内存地址
# print(stu == stu1)
# print(stu != stu1)


# 面向对象3大特性
# 封装---将现实世界的事物在类中描述为属性和方法  继承  多态
# __*** 私有化---定义不直接对用户开放的属性和行为
# class Phone(object):
#
#     __current_voltage = 0.5  # 当前手机运行电压
#
#     def __keep_single_core(self):
#         print("让CPU以单核模式运行")
#
#     def call_by_5g(self):
#         if self.__current_voltage >= 1:  # 私有成员变量的使用
#             print("5g通信已开启")
#         else:
#             self.__keep_single_core()  # 私有成员方法的使用
#             print("电量不足，无法使用5g通信，已启用单核运行")
#
#
# phone = Phone()
# # phone.__keep_single_core()
# # print(phone.__current_voltage)
# phone.call_by_5g()

# class Phone:
#
#     __is_5g_enable = True  # 5g状态（True or False)
#
#     def __check_5g(self):  # 定义方法使用def关键字
#         if self.__is_5g_enable:  # self表示对象本身
#             print("5g开启")
#         else:
#             print("5g关闭，使用4g网络")
#
#     def call_by_5g(self):
#         self.__check_5g()  # 注意self的使用
#         print("正在通话中...")
#
#
# phone = Phone()
# phone.call_by_5g()

# 继承
# class Phone:
#     IMEI = None       # 序列号
#     producer = "华为"  # 厂商
#
#     def call_by_4g(self):
#         print("4G通话")
#
#
# class NFCReader:
#     nfc_type = "第五代"
#     producer = "三星"
#
#     def read_card(self):
#         print("NFC读卡")
#
#     def write_card(self):
#         print("NFC写卡")
#
#
# class RemoteControl:
#     rc_type = "红外遥控"
#
#     def control(self):
#         print("红外遥控开启")
#
#
# # 区别java单继承多实现
# class Phone2024(Phone, NFCReader, RemoteControl):  # 属性和方法优先级：先来后到
#
#     pass
#
#     # face_id = "10010"  # 面部识别ID
#     #
#     # def call_by_5g(self):
#     #     print("5g通话")
#
#
# phone = Phone2024()
# print(phone.producer)
# phone.call_by_4g()
# # phone.call_by_5g()
# phone.read_card()
# phone.write_card()
# phone.control()


# 复写overridden
# class Phone:
#     IMEI = None       # 序列号
#     producer = "华为"  # 厂商
#
#     def call_by_5g(self):
#         print("5G通话")
#
#
# class MyPhone(Phone):
#     producer = "荣耀"
#
#     def call_by_5g(self):
#
#         # 方法一
#         # print(Phone.producer)
#         # Phone.call_by_5g(self)  # 注意self指针
#
#         # 方法二
#         print(f"父类的厂商：{super().producer}")  # super() 超类对象
#         super().call_by_5g()  # 调用父类的方法
#
#         print("开启省电模式")
#
#
# phone = MyPhone()
# print(phone.producer)
# phone.call_by_5g()


# 类型注解

# 变量
# 变量名[对象名]: 类型 = 具体值
# 注释中类型注解

# 基础数据类型
# import random
#
# var_1: int = 10
# var_2: str = "Hello"
# var_3: bool = True
#
#
# # 类对象
# class Student:
#     pass
#
#
# stu: Student = Student()
#
# # 基础容器注解
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = {"Hello": 666}
#
# # 基础容器详细注解
# my_list: list[int] = [1, 2, 3]
# my_tuple: tuple[int, str, bool] = (1, '2', True)
# my_dict: dict[str, int] = {"Hello": 666}
#
# # 注释注解
# var_1 = random.randint(1, 10)  # type: int
#
#
# def func():
#     return 0
#
#
# var_3 = func()  # type: int

# 函数（方法）进行类型注解---形参/ 返回值（提示性的）
# def add(x: int, y: int) -> int:
#     return x + y
#
#
# print(add(1, 2))

# Union类型联合注解
from typing import Union
my_list: list[Union[str, int]] = ["Hello", 123]



