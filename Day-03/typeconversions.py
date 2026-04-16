Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=3.14
type(b)
<class 'float'>
int(b)
3
complex(b)
(3.14+0j)
str(b)
'3.14'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c = 7+3j
type(c)
<class 'complex'>
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
list(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
str(c)
'(7+3j)'
tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s = 'amaan'
type(s)
<class 'str'>
int(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'amaan'
int(2)
2
r = 'amaan = 4'
int(r)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(r)
ValueError: invalid literal for int() with base 10: 'amaan = 4'
float(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'amaan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['a', 'm', 'a', 'a', 'n']
tuple(s)
('a', 'm', 'a', 'a', 'n')
set(s)
{'a', 'm', 'n'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
l = [1,2,5,6,5,2,4]
type(l)
<class 'list'>
tuple(l)
(1, 2, 5, 6, 5, 2, 4)
set(l)
{1, 2, 4, 5, 6}
dict(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
int(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> d = {'name':'amaan', 'age':22, 'course': 'python'}
>>> type(d)
<class 'dict'>
>>> list(d)
['name', 'age', 'course']
>>> tuple(d)
('name', 'age', 'course')
>>> set(d)
{'course', 'name', 'age'}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> str(d)
"{'name': 'amaan', 'age': 22, 'course': 'python'}"
>>> bool(d)
True
>>> b = 'False'
>>> int(b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: 'False'
>>> b = False
>>> b
False
>>> int(b)
0
>>> type(b)
<class 'bool'>
>>> float(b)
0.0
>>> complex(b)
0j
>>> str(b)
'False'
