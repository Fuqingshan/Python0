#插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

#不明白可以看图
#https://www.runoob.com/python3/python-insertion-sort.html

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1 #找到前一个
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j] # 交换key和key前面的一个值
            j -= 1 #j往前移动
        arr[j+1] = key #直到key大于前面的数，把key插入正确的位置

arr = [12,11,13,5,6]
insertionSort(arr)
print(f"排序后的数组：{arr}")

