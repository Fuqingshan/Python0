#del移除
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

# 输出原始的字典
print("字典移除前 : " + str(test_dict))

# 使用 del 移除 Zhihu
del test_dict['Zhihu']

# 输出移除后的字典
print("字典移除后 : " + str(test_dict))

# 移除没有的 key 会报错
# del test_dict['Baidu']