Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = []
type(l)
<class 'list'>
l = list()
l
[]
type(l)
<class 'list'>
l = [17, 98.2, 'asif', [], {}, {8:9}, True, ()]
l
[17, 98.2, 'asif', [], {}, {8: 9}, True, ()]


a = [1,2,3,4]
b = [7,8,9]
a+b
[1, 2, 3, 4, 7, 8, 9]
a*8
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


names = ['asif', 'amaan', 'syed', 'sonu', 'md']
names
['asif', 'amaan', 'syed', 'sonu', 'md']
names[3]
'sonu'
names[0]
'asif'
names[-1]
'md'
names[-4]
'amaan'
names[6]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names[6]
IndexError: list index out of range
names[1:3]
['amaan', 'syed']
names[:-1]
['asif', 'amaan', 'syed', 'sonu']
names[2:]
['syed', 'sonu', 'md']
names[2::]
['syed', 'sonu', 'md']
names[::2]
['asif', 'syed', 'md']
names[::-1]
['md', 'sonu', 'syed', 'amaan', 'asif']
names[1:5:2]
['amaan', 'sonu']
'asif' in names
True
'soha' in names
False
'sohu' not in names
True
'amaan' not in names
False
len(names)
5
sorted(names)
['amaan', 'asif', 'md', 'sonu', 'syed']
max(names)
'syed'
min(names)
'amaan'


names
['asif', 'amaan', 'syed', 'sonu', 'md']
id(names)
2088769701888
names[2]
'syed'
names[0] = 'Asif'
names
['Asif', 'amaan', 'syed', 'sonu', 'md']
id(names)
2088769701888


names.append('Soha')
names
['Asif', 'amaan', 'syed', 'sonu', 'md', 'Soha']


names.insert(3, 'Sana')
names
['Asif', 'amaan', 'syed', 'Sana', 'sonu', 'md', 'Soha']

names.extend(['Mike', 'Will', 'Max', 'Dustin'])
names
['Asif', 'amaan', 'syed', 'Sana', 'sonu', 'md', 'Soha', 'Mike', 'Will', 'Max', 'Dustin']

names.pop(5)
'md'
names
['Asif', 'amaan', 'syed', 'Sana', 'sonu', 'Soha', 'Mike', 'Will', 'Max', 'Dustin']
names.pop()
'Dustin'
names
['Asif', 'amaan', 'syed', 'Sana', 'sonu', 'Soha', 'Mike', 'Will', 'Max']

names.remove('Sana')
names
['Asif', 'amaan', 'syed', 'sonu', 'Soha', 'Mike', 'Will', 'Max']

names.remove('Soha')
names
['Asif', 'amaan', 'syed', 'sonu', 'Mike', 'Will', 'Max']

del names[2]
names
['Asif', 'amaan', 'sonu', 'Mike', 'Will', 'Max']

names.clear()
names
[]


names = ['Asif', 'amaan', 'syed', 'Sana', 'sonu', 'Soha', 'Mike', 'Will', 'Max', 'Dustin']
names
['Asif', 'amaan', 'syed', 'Sana', 'sonu', 'Soha', 'Mike', 'Will', 'Max', 'Dustin']
names.index('Dustin')
9
names.index('Asif')
0
names.index('Steve')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    names.index('Steve')
ValueError: list.index(x): x not in list


l = [1, 7, 8, 4, 3, 1, 3, 1, 6, 8, 1]
l.count(1)
4
l.count(3)
2

sorted(l)
[1, 1, 1, 1, 3, 3, 4, 6, 7, 8, 8]
l
[1, 7, 8, 4, 3, 1, 3, 1, 6, 8, 1]
l.sort()
l
[1, 1, 1, 1, 3, 3, 4, 6, 7, 8, 8]
l.sort(reverse=True)
l
[8, 8, 7, 6, 4, 3, 3, 1, 1, 1, 1]
l.reverse()
l
[1, 1, 1, 1, 3, 3, 4, 6, 7, 8, 8]


a=[1,6,4,3,7]
b=a
b
[1, 6, 4, 3, 7]
a
[1, 6, 4, 3, 7]
>>> b.append(8)
>>> b
[1, 6, 4, 3, 7, 8]
>>> a
[1, 6, 4, 3, 7, 8]
>>> 
>>> c=a.copy()
>>> c
[1, 6, 4, 3, 7, 8]
>>> c.append(5)
>>> c
[1, 6, 4, 3, 7, 8, 5]
>>> a
[1, 6, 4, 3, 7, 8]
>>> id(a)
2088769603200
>>> id(b)
2088769603200
>>> id(c)
2088769743680
>>> 
>>> 
>>> sum(c)
34
>>> len(c)
7
>>> 
>>> 
>>> # [0, 0.0, '',[], {}, set(), (), False]
>>> # [1, -1, 0.1, 'asif', [123], True]
>>> 
>>> any([0, 0.0, '',[], {}, set(), (), False])
False
>>> any([1, 0.0, '',[], {}, set(), (), False])
True
>>> all([1, 0.0, '',[], {}, set(), (), False])
False
>>> all([1, -1, 0.1, 'asif', [123], True])
True
