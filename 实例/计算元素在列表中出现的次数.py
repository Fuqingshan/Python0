'''
输入 : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
       x = 10
输出 : 3

'''


def countX(lst, x):
    return lst.count(x)


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))