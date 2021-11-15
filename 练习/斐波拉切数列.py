#斐波拉切数列值这样一个数列，0，1，1，2，3，5，8，13，第0项是0，第一项是1，第三项开始，每一项都为前两项之和

nterms=int(input("你需要几项？"))

# 第一和第二项
n1 = 0
n2 = 1
count = 2

#判断输入的数字是否合法
if nterms <= 0:
    print("请输入一个正整数")
elif nterms == 1:
    print("斐波拉切数列：")
    print(n1)
else:
    print("斐波拉切数列：")
    print(n1,",",n2, end=",")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=",")
        #更新值
        n1 = n2
        n2 = nth
        count += 1
