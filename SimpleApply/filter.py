#filter
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6,7])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['a','b',None,'  '])))

#filter取素数

#生成器，从3开始的序列
def _odd_iter():
    n = 1
    while True:
        n  =n+2
        yield  n
#筛选函数
def _not_divisible(n):
    return lambda x:x %  n > 0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible,it)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


print('########################################')
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return str(n)==str(n)[::-1] #完美，正序倒序字符串一致
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')