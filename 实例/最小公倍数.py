def lcm(x,y):
    #获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))
print(f"{num1}与{num2}的最大公倍数为{lcm(num1,num2)}")