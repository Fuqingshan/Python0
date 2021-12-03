import urllib.request
import urllib.parse
import urllib.error
import urllib.robotparser
from urllib.request import urlopen

'''
以下代码使用 urlopen 打开一个 URL，然后使用 read() 函数获取网页的 HTML 实体代码。
read() 是读取整个网页内容，我们可以指定读取的长度：.read(300)
'''
myURL = urlopen("https://www.runoob.com")
print(myURL.read(300))

print("************************************")
#readline - 读取文件的一行内容
#readlines - 读取文件的全部内容，它会把读取的内容赋值给一个列表变量
print(myURL.readline()) #读取一行内容
'''
lines = myURL.readlines()
for line in lines:
    print(line)
'''

#判断网页是否可以访问
print("是否可以访问" + f"{myURL.getcode() == 200}")

#抓取网页保存到本地,下面代码会生成一个runoob_urllib_test.html文件
with open("runoob_urllib_test.html","wb") as f:
    f.write(myURL.read())
    f.close()

#url编解码
encodeURL = urllib.request.quote("https://www.runoob.com")
print(encodeURL)
decodeURL = urllib.request.unquote(encodeURL)
print(decodeURL)

#请求头

#搜索页
url = "https://www.runoob.com?s="
keyword = "python 教程"
encodeKey = urllib.request.quote(keyword)
url = url + encodeKey
header = { 'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request).read()

with open("urllib_test_runoob_search.html","wb") as f:
    f.write(response)
    f.close()

#请求头包含data的表单
url = 'https://www.runoob.com/try/py3/py3_urllib_test.php'  # 提交到表单页面
data = {'name':'RUNOOB', 'tag' : '菜鸟教程'}   # 提交数据
header = {
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}   #头部信息
data = urllib.parse.urlencode(data).encode('utf8')  # 对参数进行编码，解码使用 urllib.parse.urldecode
request=urllib.request.Request(url, data, header)   # 请求处理
response=urllib.request.urlopen(request).read()      # 读取结果

with open("urllib_test_post_runoob.html","wb") as f:
    f.write(response)
    f.close()


#error
try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)   # 404

#parse用于解析URL
o = urllib.parse.urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o)
print(o.scheme)
'''
具体的属性可以看：https://www.runoob.com/python3/python-urllib.html 的urllib.parse部分
'''

#urllib.robotparser 用于解析 robots.txt 文件。
#robots.txt（统一小写）是一种存放于网站根目录下的 robots 协议，它通常用于告诉搜索引擎对网站的抓取规则。
#urllib.robotparser 提供了 RobotFileParser 类，
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")
rp.read()
rrate = rp.request_rate("*")
print(rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"))
print(rp.can_fetch("*", "http://www.musi-cal.com/"))