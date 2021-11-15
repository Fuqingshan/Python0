'''
定义一个整型数组，并计算元素之和。
实现要求：
输入 : arr[] = {1, 2, 3}
输出 : 6
计算: 1 + 2 + 3 = 6

'''

#定义函数，arr为数组，n为数组长度，可作为备用参数，这里没有用到
def _sum(arr, n):
    #使用内置的sum函数计算
    return sum(arr)

arr=[]
arr = [12,3,4,15]

n = len(arr)
ans = _sum(arr,n)

print(ans)