def recur_fibo(n):
    '''递归函数 输出斐波拉切数列'''
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n - 2))

#获取用户输入
n = int(input("输出几项："))

if n <= 0:
    print("输入正数")
else:
    print("斐波拉切数列：")
    for i in range(n):
        print(recur_fibo(i))