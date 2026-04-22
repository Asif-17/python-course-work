Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = set()
s = {1, 4, 6, 4, 3, 2, 1, 7, 9, 6, 5, 4}
s
{1, 2, 3, 4, 5, 6, 7, 9}
s.add(100)
s
{1, 2, 3, 4, 5, 6, 7, 100, 9}
s.add(8)
s
{1, 2, 3, 4, 5, 6, 7, 100, 9, 8}

s.add(17.2)
s
{1, 2, 3, 4, 5, 6, 7, 100, 9, 8, 17.2}
s.add('asif')
s
{1, 2, 3, 4, 5, 6, 7, 100, 9, 8, 'asif', 17.2}
s.add([7,8])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.add([7,8])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add((1,2,3))
s
{1, 2, 3, 4, 5, 6, 7, 100, 9, 8, (1, 2, 3), 'asif', 17.2}
s.add({2,5})
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.add({2,5})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')


s
{1, 2, 3, 4, 5, 6, 7, 100, 9, 8, (1, 2, 3), 'asif', 17.2}
2 in s
True
(1,2,3) in s
True
3 not in s
False

for i in s:
    print(i)

    
1
2
3
4
5
6
7
100
9
8
(1, 2, 3)
asif
17.2


a = {2,4,5,7,3}
b = {7,6,0,1,3}
a.union(b)
{0, 1, 2, 3, 4, 5, 6, 7}
a | b
{0, 1, 2, 3, 4, 5, 6, 7}
a.intersect(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.intersect(b)
AttributeError: 'set' object has no attribute 'intersect'. Did you mean: 'intersection'?
a.intersection(b)
{3, 7}
a & b
{3, 7}


a
{2, 3, 4, 5, 7}
b
{0, 1, 3, 6, 7}
a - b
{2, 4, 5}
b - a
{0, 1, 6}


a
{2, 3, 4, 5, 7}
{2} < a
True
{9} < a
False
{2,4} < a
True

a > {2, 5, 7}
True
a > {3,9,6}
False


a.isdisjoint(b)
False
c = {1,6,8,9,0}
a.isdisjoint(b)
False
a.isdisjoint(c)
True


a.update({20, 50, 64})
a
{64, 2, 3, 4, 5, 50, 7, 20}

a.remove(7)
a
{64, 2, 3, 4, 5, 50, 20}
a.remove(64)
a
{2, 3, 4, 5, 50, 20}
a.pop()
2
a.pop()
3
a
{4, 5, 50, 20}
a.discard(64)
a
{4, 5, 50, 20}


a = {40, 45, 5, 6, 3, 23}
b = {45, 60, 54, 76, 4, 2}
a.intersection(b)
{45}
a.intersection_update(b)
a
{45}


b
{2, 4, 54, 76, 45, 60}
c=b
>>> c.add(10)
>>> c
{2, 4, 54, 10, 76, 45, 60}
>>> b
{2, 4, 54, 10, 76, 45, 60}
>>> e = c.copy()
>>> e
{2, 4, 54, 10, 76, 45, 60}
>>> c
{2, 4, 54, 10, 76, 45, 60}
>>> e.add(100)
>>> e
{2, 4, 100, 54, 10, 76, 45, 60}
>>> c
{2, 4, 54, 10, 76, 45, 60}
>>> 
>>> 
>>> a
{45}
>>> b
{2, 4, 54, 10, 76, 45, 60}
>>> len(b)
7
>>> max(b)
76
>>> min(b)
2
>>> sorted(b)
[2, 4, 10, 45, 54, 60, 76]
>>> sum(b)
251
>>> 
>>> 
>>> 
>>> frozen = frozenset([1,2,3])
>>> frozen.add(10)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    frozen.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
