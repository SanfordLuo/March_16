# 使用字典保存数据,字典里面套字典
# 先定义一个空字典
all_dict = {}
def print_menu():
    """打印菜单"""
    print("---------------------------")
    print("     学生管理系统 V1.0")
    print(" 1:添加学生信息")
    print(" 2:删除学生信息")
    print(" 3:修改学生信息")
    print(" 4:查询学生信息")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")

def add_dict():
    """添加名片"""
    new_name = input("请输入您的姓名：")
    new_age = input("请输入您的年龄：")
    my_dict = {"name": new_name, "age": new_age}  # 内部字典
    all_dict[new_name] = my_dict
    print("保存数据成功……")

def del_dict():
    """删除学生信息"""
    del_name = input("请输入要删除信息的名字：")
    if del_name in all_dict:
        del all_dict[del_name]
        print("删除信息成功……")
    else:
        print("你输入的名字有误！")

def revise_dict():
    """修改学生信息"""
    revise_name = input("请输入要修改信息的名字：")
    if revise_name in all_dict:
        revise_age = input("请输入修改后的年龄：")
        all_dict[revise_name]["age"] = revise_age
        print("修改信息成功……")
    else:
        print("您输入的名字有误！")

def find_dict():
    """查询学生信息"""
    find_name = input("请输入要查询的名字：")
    if find_name in all_dict:
        print("姓名:%s 年龄:%s" % (find_name, all_dict[find_name]["age"]))
    else:
        print("您输入的名字有误……")

def print_dict():
    """显示所有学生信息"""
    for key, value in all_dict.items():
        print("姓名:%s 年龄:%s" % (key, value["age"]))

def exit_menu():
    """退出系统"""
    print("退出系统成功……")

def main():
    """主函数，完成整个程序的控制"""
    while True:
        print_menu()
        command = input("请输入选项：")
        if not command.isdigit():        # 如果command 不是数字
            print("只能输入数字1~6，请重新输入……")
            continue
        elif command == "1":
            add_dict()
        elif command == "2":
            del_dict()
        elif command == "3":
            revise_dict()
        elif command == "4":
            find_dict()
        elif command == "5":
            print_dict()
        elif command == "6":
            exit_menu()
            break
        else:
            print("只能输入数字1~6，请重新输入……")
            
main()
