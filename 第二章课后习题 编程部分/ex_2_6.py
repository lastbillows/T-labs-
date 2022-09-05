
import time as t
year=input("请输入年份")
month=input("请输入月份")
day=input("请输入日期")
date=year+'-'+month+'-'+day
print(date)
c=t.strptime(date,"%Y-%m-%d")
print ("这一天是当年的第",c.tm_yday,"天")

