import itertools
#迭代对象

#count会创建一个无限迭代器,自然数
natuals=itertools.count(1)
for n in natuals:
    print(n)

#cycle会把传入的序列无限重复
cs=itertools.cycle('abc')
for c in cs:
    print(c)

#chain()将一组迭代器串联，形成更大的迭代器
for c in itertools.chain('abc','xyz'):
    print(c)

#groupby将迭代器重复元素跳出来
