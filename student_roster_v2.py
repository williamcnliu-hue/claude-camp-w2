# 学员花名册管理器 v2 (Improved)
# Week 2 Exercise 1 - Student Roster Manager


def show_menu():
    """显示主菜单"""
    print("\n=== 学员花名册管理器 ===")
    print("1. 添加学员")
    print("2. 查询学员")
    print("3. 删除学员")
    print("4. 查看全部学员")
    print("5. 退出")


def add_student(students):
    """添加新学员（含重复检查和输入校验）"""
    name = input("请输入学员姓名: ").strip()
    if not name:
        print("⚠️ 姓名不能为空")
        return
    
    # 检查是否已存在
    if any(s["name"] == name for s in students):
        print(f"⚠️ 学员 '{name}' 已存在，未添加")
        return
    
    email = input("请输入学员邮箱: ").strip()
    if "@" not in email:
        print("⚠️ 邮箱格式不正确")
        return
    
    join_date = input("请输入加入日期: ").strip()
    
    students.append({
        "name": name,
        "email": email,
        "join_date": join_date
    })
    print(f"✅ 已添加学员: {name}")


def find_student(students):
    """查询学员"""
    search_name = input("请输入要查询的学员姓名: ").strip()
    
    for student in students:
        if student["name"] == search_name:
            print(f"✅ 找到了！")
            print(f"   姓名: {student['name']}")
            print(f"   邮箱: {student['email']}")
            print(f"   加入日期: {student['join_date']}")
            break
    else:
        # 这个 else 配对的是 for 循环，不是 if
        print(f"❌ 没找到名叫 '{search_name}' 的学员")


def delete_student(students):
    """删除学员"""
    delete_name = input("请输入要删除的学员姓名: ").strip()
    
    for student in students:
        if student["name"] == delete_name:
            students.remove(student)
            print(f"🗑️ 已删除学员: {delete_name}")
            break
    else:
        print(f"❌ 没找到名叫 '{delete_name}' 的学员")


def list_all_students(students):
    """查看全部学员"""
    if len(students) == 0:
        print("📭 还没有添加任何学员")
        return
    
    print(f"\n📋 全部学员名单（共 {len(students)} 人）：")
    for student in students:
        print(f"   姓名: {student['name']}, 邮箱: {student['email']}, 加入日期: {student['join_date']}")


def main():
    """主程序入口"""
    students = []
    
    while True:
        show_menu()
        choice = input("请选择操作 (1-5): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            find_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            list_all_students(students)
        elif choice == "5":
            print("再见！")
            break
        else:
            print("⚠️ 无效选择，请输入 1-5 之间的数字")


# 程序从这里开始运行
main()
