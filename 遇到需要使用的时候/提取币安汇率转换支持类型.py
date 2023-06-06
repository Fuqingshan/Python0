import json

bnbSymbols = []

# 读取数据
with open('bnb.json', 'r') as f:
    data = json.load(f)
    for i in data:
        bnbSymbols.append(i["symbol"])
    print(f"json文件为：{bnbSymbols}")

# 写入 JSON 数据
with open('bnb_symbols.txt', 'w') as f:
    json.dump(bnbSymbols, f)
