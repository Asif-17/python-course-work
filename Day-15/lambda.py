def equal(s1,s2):
    if s1==s2:
        return "Equal"
    else:
        return "Not Equal"

'''
res = lambda s1,s2: "Equal" if s1==s2 else "Not Equal"

s1 = 'python'
s2 = 'lang'
print(res(s1,s2))
'''

'''
res = lambda ch: "Alp" if ch.isalpha() else "Not Alp"
print(res('A'))
'''

'''
res = lambda num: num*num
print(res(20))
'''

'''
res = lambda name: f'Thankyou {name} for choosing python'

print(res('Asif'))
'''

# map - to update the entire sequence
'''
l=[1,2,3,4,5]

res=list(map(lambda i:i**2,l))

print(res)
'''

'''
l=['asif', 'amaan', 'sameer']

res=list(map(lambda i:i.upper(),l))

print(res)
'''

'''
l=[1,2,6,5,4,3]

res=list(map(lambda i:i+10,l))

print(res)
'''

'''
l=[1,2,3,4,5]

res=list(map(lambda i:i[0]*i[1],enumerate(l)))
print(res)
'''

'''
res = lambda s:s.split('@')[-1]

print(res("a.syed@iitg.ac.in"))
'''


#filter - filtering the list of elements
'''
l=[3,4,5,6,7,9,24]

res=list(filter(lambda i:i%3==0, l))
print(res)
'''

'''
l=[3,4,5,6,7,9,24]

res=list(filter(lambda i:i%2==0, l))
print(res)
'''

#reduce
'''
from functools import reduce

l=[1,4,3,6,7,4,5]

res=reduce(lambda sum,i:sum+i,l)

print(res)
'''

'''
from functools import reduce

l=[1,4,3,6,7,4,5]

res=reduce(lambda a,b:a+b,l)

print(res)
'''


