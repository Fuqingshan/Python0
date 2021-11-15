#S = πr^2

import math

#定义一个方法计算圆的面积
def findArea(r):
    pi = 3.14159
    return pi * math.pow(r,2)

print(f"圆的面积为：{findArea(5)}")
