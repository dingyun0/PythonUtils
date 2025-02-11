def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "除数不能为0"
    return a/b

def caculator():
    print("欢迎使用计算器")
    print("请选择操作：")
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    while True:
        choice=input("请输入操作：1/2/3/4:")
        if choice not in ("1","2","3","4"):
            print("输入错误，请重新输入")
            continue
        try:
            num1=float(input("请输入第一个数："))
            num2=float(input("请输入第二个数："))
        except ValueError:
            print("输入错误，请重新输入")
            continue

        if choice=="1":
            print(f"{num1}+{num2}={add(num1,num2)}")
        elif choice=="2":
            print(f"{num1}-{num2}={sub(num1,num2)}")
        elif choice=="3":
            print(f"{num1}*{num2}={mul(num1,num2)}")
        elif choice=="4":
            print(f"{num1}/{num2}={div(num1,num2)}")
        else:
            print("输入错误，请重新输入")
        
        ifContinue=input("是否继续计算？(y/n)")
        if ifContinue=="n":
            print("感谢使用，再见！")
            break

caculator()