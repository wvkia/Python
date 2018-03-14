
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def fact_nail(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num -1,num * product)


print(fact(3))
print (fact_nail(5))

l=[]
n=1
while n < 99:
    l.append(n)
    n += 2
print(l)