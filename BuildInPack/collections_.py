#简单named类型
from collections import namedtuple

Point=namedtuple('Point',['x','y']) #自定义数据类型
p=Point(1,2)
print(p.x ,'  ', p.y)

#list线性存储，访问速度快但插入删除慢，使用deque 双向列表
from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)

#dict如果key不存在，会抛出KeyError，如果希望不存在返回默认值，使用defaultdict
from collections import defaultdict
dd=defaultdict(lambda :'N/A')   #设置默认值
dd['key1']='aa'
print(dd['key1'])
print(dd['key2'])

#dict是无序的，对其做迭代无法确定key顺序
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print(d)
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)


