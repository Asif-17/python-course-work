Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# str, list, tuple, set, dict, range()

s = 'python'
for i in s:
    print(i)

    
p
y
t
h
o
n


l = [1,2,3,4]
for i in l:
    print(i)

    
1
2
3
4


t = (2, 4, 6, 5, 4)
for i in t:
    print(i)

    
2
4
6
5
4


s = {3, 5, 6, 8, 4}
for i in s:
    print(i)

    
3
4
5
6
8


d = {1:1, 2:4, 3:9, 4:16, 5:25}
for i in d:
    print(i, d[i])

    
1 1
2 4
3 9
4 16
5 25


for i in range(0,10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9


for i in range(1,10,2);
SyntaxError: invalid syntax
for i in range(1,10,2):
    print(i)

    
1
3
5
7
9


for i in range(0,11,2):
    print(i)

    
0
2
4
6
8
10


for i in range(7, 51, 7):
    print(i)

    
7
14
21
28
35
42
49


for i in range(10,0,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1


for i in range(20, 9, -1):
    print(i)

    
20
19
18
17
16
15
14
13
12
11
10


for i in range(6)
SyntaxError: expected ':'
for i in range(6):
    print(i)

    
0
1
2
3
4
5



s = 'amaan'
for i in enumerate(s):
    print(i)

    
(0, 'a')
(1, 'm')
(2, 'a')
(3, 'a')
(4, 'n')


s = 'amaan'
for i in range(len(s)):
    print(i)

    
0
1
2
3
4


s = 'amaan'
for i in range(len(s)):
    print(i, s[i])

    
0 a
1 m
2 a
3 a
4 n


names = ['syed', 'mohammad', 'asif', 'amaan']
for i in enumerate(names):
    print(i[0], i[1])

    
0 syed
1 mohammad
2 asif
3 amaan


for i in range(len(names)):
    print(i, names[i])

    
0 syed
1 mohammad
2 asif
3 amaan


s = {1,2,3}
for i in enumerate(s):
    print(i[0], i[1])

    
0 1
1 2
2 3


for i in range(len(s)):
    print(i, s[i])

    
Traceback (most recent call last):
  File "<pyshell#107>", line 2, in <module>
    print(i, s[i])
TypeError: 'set' object is not subscriptable


d = {1:1, 2:4, 3:9}
for i in enumerate(d):
    print(i)

    
(0, 1)
(1, 2)
(2, 3)


d = {1:1, 2:4, 3:9}
for i in enumerate(d):
    print(i[0], i[1], d[i[1]])
    
SyntaxError: multiple statements found while compiling a single statement


d = {1:1, 2:4, 3:9, 4:16}
for i in enumerate(d):
    print(i[0], i[1], d[i[1]])
    
SyntaxError: multiple statements found while compiling a single statement


d = {1:1, 2:4, 3:9, 4:16}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])
    
SyntaxError: multiple statements found while compiling a single statement


d = {1:1, 2:4, 3:9, 4:16}
for i in enumerate(d):
    print(i[0], i[1], d[i[1]])

    
0 1 1
1 2 4
2 3 9
3 4 16


for i in range(10):
    pass


for i in range(10):
    if i==5:
        break
    print(i)

    
0
1
2
3
4
>>> 
>>> 
>>> for i in range(10):
...     if i == 5:
...         continue
...     print(i)
... 
...     
0
1
2
3
4
6
7
8
9
>>> 
>>> 
>>> 
========================================= RESTART: C:/Users/amaan/OneDrive/Desktop/Python/Day-10/for_ifelse_statements.py =========================================
Not Found
>>> 
========================================= RESTART: C:/Users/amaan/OneDrive/Desktop/Python/Day-10/for_ifelse_statements.py =========================================
laptop
>>> 
========================================= RESTART: C:/Users/amaan/OneDrive/Desktop/Python/Day-10/for_ifelse_statements.py =========================================
Enter the pin: 123
Incorrect pin
Enter the pin: 125
Incorrect pin
Enter the pin: 1239
Incorrect pin
Enter the pin: 12786
Incorrect pin
Enter the pin: 12098
Incorrect pin
Try again after 60 seconds
