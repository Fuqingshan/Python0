#拓扑排序

'''
对一个有向无环图(Directed Acyclic Graph简称DAG)G进行拓扑排序，是将G中所有顶点排成一个线性序列，使得图中任意一对顶点u和v，若边(u,v)∈E(G)，
则u在线性序列中出现在v之前。通常，这样的线性序列称为满足拓扑次序(Topological Order)的序列，简称拓扑序列。简单的说，
由某个集合上的一个偏序得到该集合上的一个全序，这个操作称之为拓扑排序。
在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）：
每个顶点出现且只出现一次；
若A在序列中排在B的前面，则在图中不存在从B到A的路径。

入度：设有向图中有一结点v，其入度即为当前所有从其他结点出发，终点为v的的边的数目。也就是所有指向v的有向边的数目。
出度：设有向图中有一结点v，其出度即为当前所有起点为v，指向其他结点的边的数目。也就是所有由v发出的边的数目。
'''
#官方答案是错的：https://www.runoob.com/python3/python-topological-sorting.html

class Solution:
    def topoSort(self,num,prerequisites):
        degree = [0]*num
        #二维数组用*初始化是同一块内存地址，改变一个，就会改变所有，使用时会有问题，而range方式则不会
        #edge = [[]]*num
        edge = [[] for i in range(num)]
        for i in range(0,num):
            degree[prerequisites[i][0]] += 1
            edge[prerequisites[i][1]].append(prerequisites[i][0])

        stack = []
        result = []

        for i in range(0,num):
            if degree[i] == 0:
                stack.append(i)

        while len(stack) > 0 :
            nIndex = stack.pop()
            degree[nIndex] -= 1
            result.append(nIndex)
            subItems = edge[nIndex]
            #把栈中没有前置课程的最顶部的放入排序数组
            for i in subItems:
                degree[i] -= 1
                if degree[i] == 0:
                    stack.append(i)

        if len(result) != num:
            print("不存在有向无环图")
            return

        print(f"有向无环图为：{result}")

s = Solution()
p = []
p.append([0,5])
p.append([0,4])
p.append([2,5])
p.append([1,4])
p.append([3,2])
p.append([1,3])

s.topoSort(6,p)
