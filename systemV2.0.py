users = []
# 当前在线用户
online_user = {}
while True:
    print("----欢迎使用 用户注册登录系统v2.0----")
    print("1.注册")
    print("2.登录")
    print("3.注销登录")
    print("4.退出程序")
    print("------------------------------------")
    command = input("请输入选择项:")

    if command == "1":
        while True:
            id = input("请输入账号：")
            if len(id) < 6 or len(id) > 20:
                print("账号长度需要6~20个字符，请重新输入！")
                continue
            else:
                break
        while True:
            pwd = input("请输入密码：")
            if len(pwd) < 8 or len(pwd) > 20:
                print("密码长度需要8~20个字符，请重新输入！")
                continue
            else:
                break
        nickname = input("请输入昵称：")
        age = input("请输入年龄：")
        info = {}
        info["id"] = id
        info["pwd"] = pwd
        info["nickname"] = nickname
        info["age"] = age
        users.append(info)
        print("注册成功！")

    elif command == "2":
        if len(online_user) != 0:
            print("已经登录了一个账号%s,请先注销" % online_user["id"])
            continue
        id = input("请输入账号：")
        pwd = input("请输入密码：")
        for user in users:
            if user["id"] == id and user["pwd"] == pwd:
                print("登录成功！")
                online_user = user
                break
        else:
            print("登录失败，账号或密码错误")

    elif command == "3":
        if len(online_user) != 0:
            online_user = {}
            print("注销成功")
        else:
            print("您还未登录")

    elif command == "4":
        print("退出程序")
        break
