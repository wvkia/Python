#函数实现Fibonacci
def fib(max):
    n,a,b=0,0,1
    while n < max:
        print (b)
        a,b=b,a+b
        n = n+1
    return 'done'

fib(8)

#函数变成生成器
def fib_g(max):
    n,a,b=0,0,1
    while n < max:
        yield b     #通过yield将函数变成生成器
        a,b=b,a+b
        n = n+1
    return 'done'

#实例yield生成器
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('ste3')
    yield (3)
#测试
o=odd()
for x in o:
    print(x)


#拿到生成器的return返回值
print('#########################')
g=fib_g(5)
while True:
    try:
        x=next(g)
        print('g: ',x)
    except StopIteration as e:
        print('Generator return value :' ,e.value)
        break
