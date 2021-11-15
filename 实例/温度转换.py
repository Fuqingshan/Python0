#用户输入摄氏度

celsius= float(input('输入摄氏度：'))

#计算华氏温度
fahrenheit= (celsius * 1.8) + 32
print("%.1f 摄氏度转为华氏温度 %.1f"%(celsius,fahrenheit))