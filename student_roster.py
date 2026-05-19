# 学员花名册管理器
# Week 2 Exercise 1 - Student Roster Manager

# 1. 准备一个空列表，用来装所有学员
students = []

# 2. 写一个主循环，一直跑到用户选择退出
while True:
    # 显示菜单
    print("\n=== 学员花名册管理器 ===")
    print("1. 添加学员")
    print("2. 查询学员")
    print("3. 删除学员")
    print("4. 查看全部学员")
    print("5. 退出")
    
    choice = input("请选择操作 (1-5): ")
    
    # 根据用户选择执行不同的操作
    if choice == "1":
        # 添加学员
        name = input("请输入学员姓名: ")
        email = input("请输入学员邮箱: ")
        join_date = input("请输入加入日期: ")
        # 把这个学员的信息打包成字典，加进列表
        students.append({"姓名": name, "邮箱": email, "加入日期": join_date})
        print(f"✅ 已添加学员: {name}")
    
    elif choice == "2":
        # 查询学员
        search_name = input("请输入要查询的学员姓名: ")
        found = False
        for student in students:
            if student["姓名"] == search_name:
                print(f"✅ 找到了！")
                print(f"   姓名: {student['姓名']}")
                print(f"   邮箱: {student['邮箱']}")
                print(f"   加入日期: {student['加入日期']}")
                found = True
                break
        if not found:
            print(f"❌ 没找到名叫 '{search_name}' 的学员")
    
    elif choice == "3":
        # 删除学员
        delete_name = input("请输入要删除的学员姓名: ")
        found = False
        for student in students:
            if student["姓名"] == delete_name:
                students.remove(student)
                print(f"🗑️ 已删除学员: {delete_name}")
                found = True
                break
        if not found:
            print(f"❌ 没找到名叫 '{delete_name}' 的学员")
    
    elif choice == "4":
        # 查看全部学员
        if len(students) == 0:
            print("📭 还没有添加任何学员")
        else:
            print(f"\n📋 全部学员名单（共 {len(students)} 人）：")
            for student in students:
                print(f"   姓名: {student['姓名']}, 邮箱: {student['邮箱']}, 加入日期: {student['加入日期']}")
    
    elif choice == "5":
        print("再见！")
        break
    
    else:
        print("⚠️ 无效选择，请输入 1-5 之间的数字")