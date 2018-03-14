import functools
def now():
    print('2018-2-10')

print(now.__name__)
def log(func):
    @functools.wraps(func ) #只需记住在定义wrapper()的前面加上@functools.wraps(func)即可，防止返回函数基本属性改变
    def wrapper(*args,**kwargs):
        print('call %s(): '% func.__name__)
        return func(*args,**kwargs);
    return wrapper
print('#############decorator###############')
@log
def now_1():
    print('2018-2-10')

now_1()


print('##############################################')

import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start=time.time()
        fn(*args,**kwargs)
        end=time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


