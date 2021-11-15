def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 0
    return x / y

print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input("请输入你的选择(1-2-3-4)：")
n1 = int(input("请输入第一个数字："))
n2 = int(input("请输入第二个数字："))

if choice == '1':
    print(f"{n1}+{n2}={add(n1,n2)}")
elif choice == '2':
    print(f"{n1}-{n2}={subtract(n1,n2)}")
elif choice == '3':
    print(f"{n1}*{n2}={multiply(n1,n2)}")
elif choice == '4':
    print(f"{n1}/{n2}={divide(n1,n2)}")
else:
    print("非法输入")


