#希尔排序
'''
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
'''

#https://www.bilibili.com/video/BV1rE411g7rW?from=search&seid=7868351194969219988&spm_id_from=333.337.0.0

def shellSort(arr):
    n = len(arr)
    gap = int(n/2) #gap 为间隔，通常取一半进行分组，每次间隔折半，>>1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                #根据当前 gap 间隔和条件进行插入排序前的后移
                arr[j] = arr[j-gap]
                j -= gap
            #组内做插入排序，插入到当前位置
            arr[j] = temp
        gap = int(gap/2)
arr = [1,2,34,53,221]
shellSort(arr)
print(f"排序之后为：{arr}")

