#去除字符串前后空格
def trim(s):
    while s[:1] ==' ':
        s=s[1:]
    while s[-1:] ==' ':
        s=s[:-1]
    return s

print(trim('       asdf            '))

#判断是否可以迭代
from collections import Iterable
print(isinstance('adsf',Iterable))  #str是否可以迭代
print(isinstance([23,4,5,5],Iterable))  #list是否可以迭代
print(isinstance((34,45),Iterable)) #turple是否可以迭代
print(isinstance(234,Iterable)) #整数是否可以迭代

#查找list中大最大值和最小值，并返回一个tuple
def findMinAndMax(L):
    if  L == []:
        return None, None
    max=min=L[0]

    for x in L[1:]:
        if max < x:
            max=x
        if min > x:
            min=x
    return (min,max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
