def check(string, sub_str):
    if string.find(sub_str) == -1:
        print("不存在")
    else:
        print("存在")
string = "www.baidu.com"
sub_str= "baidu"
check(string, sub_str)