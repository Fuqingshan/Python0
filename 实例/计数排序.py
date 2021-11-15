#计数排序
'''
计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
'''

#https://www.runoob.com/python3/python-counting-sort.html

#官方的，感觉这样做复杂了
def countSort(arr):
    output = [0 for i in range(256)] #生成长度为256，默认值为0的数组
    count = [0 for i in range(256)] #生成长度为256，默认值为0的数组
    ans = ["" for _ in arr] #生成长度为len(arr),内容为""的数组

    # 以arr中内容的ASCII值作为下标放入count中
    for i in arr:
        count[ord(i)] += 1
    for i in range(256):
        count[i] += count[i-1]
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

arr = "www.baidu.com"
ans = countSort(arr)
j = "".join(ans)
print(f"字符串排序之后为：{j}")

#字典的方式
def countSortByDictionary(arr):
    dic = {}
    for i in arr:
        k = str(i)
        if k in dic.keys():
            dic[k] += 1
        else:
            dic[k] = 1
    li = list(dic.keys())
    li.sort()
    for i in li:
        for _ in range(0,dic[i]):
            print(i,end="")

arr = "www.baidu.com"
countSortByDictionary(arr)