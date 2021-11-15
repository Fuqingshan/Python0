a=float(input("输入三角形第一边长："))
b=float(input("输入三角形第二边长："))
c=float(input("输入三角形第三边长："))

#计算半周长
s = (a+b+c)/2

#计算面积
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(f"三角形面积：{area}")