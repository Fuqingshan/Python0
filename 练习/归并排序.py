#归并排序

'''
归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

分治法:
分割：递归地把当前序列平均分割成两半。
集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
'''

#归并算法
def merge(arr, l, m, r):
    n1 = m - l + 1 #分隔之后前面的个数
    n2 = r - m #分隔之后后面的个数

    #创建临时数组
    L = [0] * n1 #创建n1长度的数组，默认值0
    R = [0] * n2

    #拷贝数组到临时数组arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m+ 1 + j]
    #归并临时数组到arr[l..r]
    i = 0 #初始化第一个数组的索引
    j = 0 #初始化第二个数组的索引
    k = l #初始化归并子数组的索引

    #归并到一个数组中
    while i < n1 and j < n2:
        #排序
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    #归并之后，第一个数组或第二个数组没有拷贝完的，要合并进去
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

#归并排序，把数组拆分成足够细的颗粒，然后对每个拆分的数组分成左右两个数组排序，再合并，最终把所有的合并之后就是排好的数组
def mergeSort(arr,l,r):
    if l < r:
        #计算出中间数的下标
        m = int( (l+r-1)/2 )
        #先将左边拆分
        mergeSort(arr,l,m)
        #再将右边拆分
        mergeSort(arr,m+1,r)
        #归并
        merge(arr,l,m,r)

arr = [12,11,13,5,6,7,90]
n = len(arr)
mergeSort(arr,0,n -1)
print(f"排序后的数组为：{arr}")