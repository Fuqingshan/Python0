import json
import requests
import re
from  bs4 import  BeautifulSoup

url = 'http://www.cntour.cn/'
strHtml = requests.get(url)
if strHtml.status_code == 200:
    print(strHtml.text)
else:
    print("请求出错啦")

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
From_data={'i':'我愛中國','from':'zh-CHS','to':'en','smartresult':'dict','client':'fanyideskweb','salt':'15477056211258','sign':'b3589f32c38bc9e3876a570b8a992604','ts':'1547705621125','bv':'b33a2f3f9d09bde064c9275bcb33d94e','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_REALTIME','typoResult':'false'}
response = requests.post(url,data=From_data)
content = json.loads(response.text)
if response.status_code == 200 & content['errorCode'] == 0:
    print(content)
    # 打印翻译后的数据
    print(content['translateResult'][0][0]['tgt'])
else:
    print("请求出错啦")


url='http://www.cntour.cn/'
proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
strhtml=requests.get(url,proxies)
soup = BeautifulSoup(strhtml.text,"lxml")
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
print(data)

for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href'),
        'ID': re.findall('\d+', item.get('href'))
    }
print(result)