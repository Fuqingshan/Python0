#堆排序
'''
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
堆排序可以说是一种利用堆的概念来排序的选择排序。
'''
#https://www.runoob.com/python3/python-heap-sort.html

#最大堆
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1 #左孩子节点
    r = 2 * i + 2 #右孩子节点
    #如果根节点小于左子节点
    if l < n and arr[i] < arr[l]:
        largest = l
    #如果最大节点小于右子节点
    if r < n and arr[largest] < arr[r]:
        largest = r
    #如果最大节点不是父节点
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]

        heapify(arr,n,largest)

def heapSort(arr):
    n = len(arr)
    #创建最大堆
    for i in range(n,-1,-1):
        heapify(arr, n, i)
    print(f"最大堆为：{arr}")
    #一个一个交换元素，每次把最大堆的最大数（顶部0）交换到最后一个位置，然后重新构建除最后一位的最大堆
    for i in range(n-1, 0, -1):
        arr[i],arr[0] = arr[0],arr[i] #交换
        heapify(arr, i , 0)
    print(f"交换之后的数组为：{arr}")

arr = [12,11,13,5,6,7,9]

heapSort(arr)
print(f"排序后：{arr}")


