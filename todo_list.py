# 待办事项清单（带文件保存）
# Week 2 Exercise 3 - Todo List with File Storage

import json

# 文件名常量
TODO_FILE = "todos.json"

# 1. 从文件加载已有的待办事项
def load_todos():
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # 文件不存在是正常情况（第一次运行）
        return []
    except json.JSONDecodeError:
        # 文件损坏，返回空列表
        print("⚠️ 待办文件似乎损坏，从空清单开始")
        return []

# 2. 把待办事项保存到文件
def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

# 3. 主程序开始
todos = load_todos()
print(f"📂 已加载 {len(todos)} 个待办事项")

while True:
    print("\n=== 待办事项清单 ===")
    print("1. 查看清单")
    print("2. 添加待办")
    print("3. 完成待办（删除）")
    print("4. 退出")
    
    choice = input("请选择操作 (1-4): ")
    
    if choice == "1":
        # 查看清单
        if len(todos) == 0:
            print("📭 待办清单为空，赶紧加点吧！")
        else:
            print(f"\n📋 待办清单（共 {len(todos)} 项）：")
            for i, todo in enumerate(todos, start=1):
                print(f"  {i}. {todo}")
    
    elif choice == "2":
        # 添加待办
        new_todo = input("请输入待办事项: ")
        todos.append(new_todo)
        save_todos(todos)
        print(f"✅ 已添加: {new_todo}")
    
    elif choice == "3":
        # 完成待办
        if len(todos) == 0:
            print("📭 清单是空的，没东西可完成")
        else:
            print("\n当前清单：")
            for i, todo in enumerate(todos, start=1):
                print(f"  {i}. {todo}")
            try:
                index = int(input("请输入要完成的待办编号: "))
                if 1 <= index <= len(todos):
                    completed = todos.pop(index - 1)
                    save_todos(todos)
                    print(f"🎉 已完成: {completed}")
                else:
                    print("❌ 编号不存在")
            except ValueError:
                print("❌ 请输入数字")
    
    elif choice == "4":
        print("再见！")
        break
    
    else:
        print("⚠️ 无效选择，请输入 1-4 之间的数字")
        