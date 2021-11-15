#list定义
print("定义")
li = ['a','b','mpilgrim','z','example']
print(li)
print(li[1])

#list 负数索引
print("负数索引")
print(li[-1])
print(li[-3])
print(li[1:3])
print(li[1:-1])
print(li[0:3])

#list 增加元素
print("增加元素")
li.append('new')
print(li)
li.insert(2,'new2')
print(li)
li.extend(["two", "elements"])
print(li)

#list 搜索
print("搜索")
print( li.index("example"))
print( li.index("new"))
# print( li.index("c"))
print( 'c' in li)

#list 删除元素
li.remove("z")
print(li)

li.remove('new')
print(li)

print(li.pop())#删除最后一个元素，然后返回删除元素的值


#list 运算符
print("运算符")
li = ['a','b','mpilgrim']
print(li)

li = li + ['example', 'new']
print(li)

li += ['two']
print(li)

li = [1,2] * 3
print(li)

#使用join链接list成字符串
#join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
print("使用join链接list成字符串")
li = ["www","baidu","com"]
print(".".join(li))
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(";".join(["%s=%s" % (k,v) for k,v in params.items()]))

#分隔字符串
print("分隔字符串")
#split 接受一个可选的第二个参数, 它是要分割的次数。
str = "www.baidu.com"
print(str.split("."))

#list 的映射解析
print("映射解析")
li = [1,9,8,4]
print([elem * 2 for elem in li])

# dictionary的解析
print("dictionary 的解析")
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
print([v for k,v in params.items()])

#list 过滤
li = ['a','b','c','dddd','e']
print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "d"])


