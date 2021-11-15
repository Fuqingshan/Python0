#判断字符串是否为数字

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import  unicodedata
        unicodedata.numeric(s)
        return True

    except (TypeError, ValueError):
        pass

    return False

#测试
print(is_number('foo'))  # False
print(is_number('1'))  # True
print(is_number('1.3'))  # True
print(is_number('-1.37'))  # True
print(is_number('1e3'))  # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四'))  # True
# 版权号
print(is_number('©'))  # False

print("*****************")
#Python isdigit() 方法检测字符串是否只由数字组成。
#Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
print('foo'.isdigit())  # False
print('1'.isdigit())  # True
print('1.3'.isdigit())  # False
print('-1.37'.isdigit())  # False
print('1e3'.isdigit())  # False

# 测试 Unicode
print('*****************')
print('٥'.isnumeric())  # True
# 泰语 2
print('๒'.isnumeric())  # True
# 中文数字
print('四'.isnumeric())  # True
# 版权号
print('©'.isnumeric())  # False