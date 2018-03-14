
#函数本身作为变量
def add(x,y,f):
    return f(x)+f(y)
print(add(-1,9,abs))

print('################################')
from functools import  reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x,y):
        return  x*10 +y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
print(str2int('234234'))
print('################################')
def char2num(s):
    return DIGITS[s]
def str2intLam(s):
    return reduce(lambda x,y:x*10 +y,map(char2num,s))
print(str2intLam('23'))

#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    s=name[0].upper()+name[1:].lower()
    return s
#测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def multi(x,y):
        return x*y
    return reduce(multi,L)
    #或者lamda表达式形式
    #return reduce(lambda x,y:x*y,L)
#测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    
    pass
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
