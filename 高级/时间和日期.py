import time

ticks = time.time()
print ("当前时间戳为:", ticks)

localtime = time.localtime(ticks)
print ("本地时间为 :", localtime)

#格式化
localtime = time.asctime( localtime )
print ("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

#返回与格林时间的偏移
print ("time.altzone %d " % time.altzone)

print(time.perf_counter())  # 返回系统运行时间
print(time.process_time())  # 返回进程运行时间

#time.ctime([secs])作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print ("time.ctime() : %s" % time.ctime())

print ("\nStart : %s" % time.ctime())
time.sleep( 1 )
print ("\nEnd : %s" % time.ctime())

import calendar

#是否是闰年
print(f"是否是闰年：{calendar.isleap(2021)}")

#年月日历
cal = calendar.month(2021,12)
print("输出2021年12月的日历：")
print(cal)

#2 表示 2021 年 12 月份的第一天是周3，30 表示 2021 年 12 月份总共有 31 天
print(calendar.monthrange(2021, 12))

#返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
print(calendar.weekday(2021,12,3))