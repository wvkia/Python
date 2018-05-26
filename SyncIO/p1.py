'''
https://zhuanlan.zhihu.com/p/31634491
https://zhuanlan.zhihu.com/p/31410589
https://www.zhihu.com/question/20511233?rf=23290260
https://zhuanlan.zhihu.com/p/27519705
https://zhuanlan.zhihu.com/hinus
'''


def consumer():
	r=''
	while True:
		print(r+' asdf')
		n=yield r
		if not n:
			return
		print('[Consumer] Consuming %s ... ' % n)
		r='200 ok'

def produce(c):
	c.send(None)
	n=0
	while n < 5:
		n = n+1
		print('[Produce] Produceing %s ... ' % n)
		r = c.send(n)
		print('[Produce] Consumer return : %s ' % r)
	c.close()

c=consumer()
produce(c)

'''
分析协程运行
通过yield关键字，consumer成了一个生成器
在yield下通过send启动生成器，第一次必须为none

将consumer传给produce后，
1、调用 c.send(None)启动生成器
2、程序切换到consumer运行，运行到yield时，暂停住，等待send方法发送数据，
3、这时候程序切换到produce继续执行，n=n+1,打印，给c生成器发送send，然后切换到consumer
4、这时候yield做的动作有两个，一个是将接收的参数传给 = 前面的变量，声明需要return给send方法的变量，也就是r
然后consumer继续执行，r=200ok,又运行到yield，这时候把r返回给send方法，同时程序切换到produce
5、produce接收到返回的信息，继续同上步骤

注意生成器函数和协程非常相似：
+ 可yield多次
+ 有多个入口点
+ 执行可以被暂停
但唯一的不同
+ 生成器函数不能控制yields后应该从哪继续执行，控制权总是被转移到生成器的调用者

python通过生成器实现协程
'''

'''
解释 send方法
'''
def MyGenerator():
	value = yield 1
	yield value
	print('I\'m finished')

gen=MyGenerator()
print(next(gen))
print(gen.send('i am value'))
print(gen.send(None))

'''
运行
1
i am value
i am finished

报错 type not callable

首先通过next()来启动生成器，也可以通过send(None)启动，到yield 1时，暂停，返回1，打印，然后send了i am value,
继续到了yield返回value也即是i am value，打印，继续send none ，从yield继续，打印 i am finished
然后生产器没有继续可以执行的了，就会抛出错误
抛出错误来说，可以通知我们生成器已经执行完毕，用来判断
'''
