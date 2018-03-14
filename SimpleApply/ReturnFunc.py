#可变函数求和
def calc_sum(*args):
    ax=0
    for n in args:
        ax +=n
    return ax

#返回求和函数
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax +=n
        return ax
    return sum

f=lazy_sum(1,2,3,4)
#打印函数
print(f)

#（）进行函数求值
print(f())


#闭包Closure，
#我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）

print('#########################################')
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
#上面三个函数全部返回都是9，而不是1，4，9
#原因在于返回的函数引用了变量i，但i并不是立刻执行，而是等到3个函数都返回，它们引用的i都变成了3，因此结果都是9

#因此，返回闭包函数时：返回函数不要引用任何循环变量，或者后续会发生变化的变量

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
print('##########正确使用闭包##################')
def count_i():
    def f(j):
        def g():
            return  j * j
        return g
    fs=[]
    for i in range (1,4):
        fs.append(f(i)) #f(i)被立即执行，因为i的当前值被传入f()
    return fs
#测试代码
f1,f2,f3=count_i()
print(f1())
print(f2())
print(f3())

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
print('##########################')
def createCounter():
    def g():    #利用一个函数做一个生成器
        n = 0
        while True:
            n = n+1
            yield n
    it=g()
    def counter():
        return next(it)
    return counter

#python引用变量的顺序：当前作用域局部变量-》外层作用域变量-》当前模块中的全局变量-》python内置变量
def createCounter_list():
    count=[0]   #list，dic是可变数据类型，
                        #整形int，浮点型float、字符串str、元祖tuple不可变数据类型
    def counter():
        count[0] +=1    #因为count是list，所以可变，count的值在改变但地址不变
        return count[0]
    return counter

def createCounter_nonlocal():
    count = 0
    def counter():
        nonlocal count  #nonlocal用于函数或者其他作用域中修改外层（非全局）变量
                                    #global用于修改全局变量
        count +=1
        return count
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

