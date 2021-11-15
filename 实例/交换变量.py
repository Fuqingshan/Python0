#用户输入

x = input("输入x的值：")
y = input("输入y的值：")

#创建临时变量，并交换
temp = x
x = y
y = temp
print(f"交换之后的变量x 为 {x}, y 为 {y}")

#利用元组交换
x,y = y,x
print(f"元组交换之后的变量x 为 {x}, y 为 {y}")
