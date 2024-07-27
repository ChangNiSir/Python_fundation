money = 5000000
name = input("请输入您的姓名：\n")


def query(show_header):
    if show_header:
        print("----------查询余额------------")
    print(f"{name}您好，您的余额为{money}")


def saving(num):
    global money
    money += num
    print("----------存额------------")
    print(f"{name}您好，您已存入{num}元")
    query(False)


def get_money(num):
    global money
    money -= num
    print("----------取额------------")
    print(f"{name}您好，您已取出{num}元")
    query(False)


def menu():
    print("-----------主菜单----------")
    print(f"{name}你好，欢迎来到西红市银行，请选择操作")
    print("查询余额\t\t[请输入1]")
    print("存款\t\t[请输入2]")
    print("取款\t\t[请输入3]")
    print("退出\t\t[请输入4]")
    return input("请输入操作：")


while True:
    keyboard_input = menu()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("请问您想要存多少钱："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请问取多少钱："))
        if num > money:
            print("余额不足，退出系统")
            break
        get_money(num)
        continue
    else:
        print("程序退出")
        break

