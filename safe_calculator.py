# 安全的计算器
# Week 2 Exercise 4 - Safe Calculator

print("=== 安全计算器 ===")
print("支持 + - × ÷ 四则运算")
print("输入 quit 随时退出\n")

while True:
    # 1. 读取第一个数字
    num1_input = input("请输入第一个数字（或 quit 退出）: ")
    if num1_input.lower() == "quit":
        print("👋 再见！")
        break
    
    try:
        num1 = float(num1_input)
    except ValueError:
        print("❌ 这不是一个有效的数字，请重新输入\n")
        continue
    
    # 2. 读取运算符
    operator = input("请输入运算符 (+, -, *, /): ")
    if operator not in ["+", "-", "*", "/"]:
        print(f"❌ '{operator}' 不是有效的运算符\n")
        continue
    
    # 3. 读取第二个数字
    num2_input = input("请输入第二个数字: ")
    if num2_input.lower() == "quit":
        print("👋 再见！")
        break
    
    try:
        num2 = float(num2_input)
    except ValueError:
        print("❌ 这不是一个有效的数字，请重新输入\n")
        continue
    
    # 4. 执行运算
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2  # 除以0会触发 ZeroDivisionError
        
        print(f"✅ 结果: {num1} {operator} {num2} = {result}\n")
    
    except ZeroDivisionError:
        print("❌ 不能除以 0！数学课没教过吗 😅\n")
    
    except Exception as e:
        # 兜底：捕获所有其他意外错误
        print(f"❌ 出现了未知错误: {e}\n")
        