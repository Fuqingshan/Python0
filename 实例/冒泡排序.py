#冒泡排序

'''
冒泡排序（Bubble Sort）也是一种简单直观的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
'''

def bubbleSort(arr):
    n = len(arr)
    #一层遍历
    for i in range(n):
        #内循环
        for j in range(0, n - i - 1):
            #如果后面的元素小于前面，则交换
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [64,34,25,12,22,11,90]

bubbleSort(arr)
print(f"排序后的数组为：{arr}")