'''
计算公式 1^3 + 2^3 + 3^3 + 4^3 + …….+ n3
实现要求：
输入 : n = 5
输出 : 225
公式 : 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225

输入 : n = 7
输入 : 784
公式 : 1^3 + 2^3 + 3^3 + 4^3 + 5^3 + 6^3 + 7^3 = 784

'''

def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i*i*i
    return  sum
n = 5
print(sumOfSeries(n))