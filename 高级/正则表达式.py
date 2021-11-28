import re

#match re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

#re.search 扫描整个字符串并返回第一个成功的匹配。

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

'''
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。
'''

#Python 的re模块提供了re.sub用于替换字符串中的匹配项。
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

#compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print( m )

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print( m )

m = pattern.match('one12twothree34four', 3, 10).span() # 从'1'的位置开始匹配，正好匹配
print( m )                                        # 返回一个 Match 对象

#findall
'''
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
注意： match 和 search 是匹配一次 findall 匹配所有。
'''
result1 = re.findall(r'\d+', 'runoob 123 google 456')

pattern = re.compile(r'\d+')  # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)
print(result3)

#返回元组
result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)

#re.finditer
#和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )


#re.split
#split 方法按照能够匹配的子串将字符串分割后返回列
p = re.split('\W+', 'runoob, runoob, runoob.')
print(p)
p = re.split('(\W+)', ' runoob, runoob, runoob.')
print(p)
p = re.split('\W+', ' runoob, runoob, runoob.', 1)
print(p)

