Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = ()
t = tuple()
type(t)
<class 'tuple'>

t = (2, 5, 8, 6, 5)
t
(2, 5, 8, 6, 5)

l = (3, 7.3, 67, 'asif', (), {}, [], {1:'amaan'})
l
(3, 7.3, 67, 'asif', (), {}, [], {1: 'amaan'})

a = (6, 8, 5)
b = (9, 2, 3, 7)
a + b
(6, 8, 5, 9, 2, 3, 7)
a * 7
(6, 8, 5, 6, 8, 5, 6, 8, 5, 6, 8, 5, 6, 8, 5, 6, 8, 5, 6, 8, 5)
b * 2
(9, 2, 3, 7, 9, 2, 3, 7)

l
(3, 7.3, 67, 'asif', (), {}, [], {1: 'amaan'})
l[2:6]
(67, 'asif', (), {})
l[1:4]
(7.3, 67, 'asif')
l[-6:]
(67, 'asif', (), {}, [], {1: 'amaan'})
l[5]
{}
l[-1]
{1: 'amaan'}
l[-4]
()
l[:-1]
(3, 7.3, 67, 'asif', (), {}, [])

'asif' in l
True
'amaan' in l
False

len(l)
8
max(l)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 
>>> 
>>> c = (3, 5, 4, 3, 7, 5, 8)
>>> max(c)
8
>>> min(c)
3
>>> sorted(c)
[3, 3, 4, 5, 5, 7, 8]
>>> c.count(3)
2
>>> sum(c)
35
>>> c.index(4)
2
>>> c.index(3)
0
>>> c.rindex(3)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    c.rindex(3)
AttributeError: 'tuple' object has no attribute 'rindex'. Did you mean: 'index'?
>>> 
>>> 
>>> t = (1,2,3,[4,5])
>>> t
(1, 2, 3, [4, 5])
>>> t.append(10)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    t.append(10)
AttributeError: 'tuple' object has no attribute 'append'
>>> t[3]
[4, 5]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 10])
>>> t[3].pop()
10
