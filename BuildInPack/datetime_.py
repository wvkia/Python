#获取当前时间
from datetime import datetime
from datetime import timedelta

now=datetime.now()
print(now)

#构造指定时间
dt=datetime(2014,3,3,23,4)
print(dt)

#时间转成timestamp
print(dt.timestamp())
#timestamp转时间
t=1429417200.0
print(datetime.fromtimestamp(t))
#时区问题
print(datetime.fromtimestamp(t))    #本地时区
print(datetime.utcfromtimestamp(t)) #UTC标准时区


#字符串
cday=datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(datetime.now().strftime('%a,%b %d %H:%M'))

#时间操作
now=datetime.now()
now = now+timedelta(hours=10)
print(now)
now=now - timedelta(days=2,hours=2)
print(now)