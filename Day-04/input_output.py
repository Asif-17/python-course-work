Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
amaan
name
'amaan'
type(name)
<class 'str'>
name = input("Enter the name: ")
Enter the name: Amaan
name
'Amaan'
age = input()
22
age
'22'
age = int(input("Enter your age: "))
Enter your age: 22
age
22
price = float(input("Enter price: "))
Enter price: 43.50
price
43.5
'asif amaan syed md'.split(' ')
['asif', 'amaan', 'syed', 'md']
'1 2 3 4 5 6'.split()
['1', '2', '3', '4', '5', '6']
'java,python,html,css,javascript'.split(', java python html css javascript')
['java,python,html,css,javascript']
'java,python,html,css,javascript'.split(' ')
['java,python,html,css,javascript']
'java python html css javascript'.split(',')
['java python html css javascript']
'java python html css javascript'.split(' ')
['java', 'python', 'html', 'css', 'javascript']
lang = input("Enter the lang: ").split()
Enter the lang: Java C++ Python HTML
lang
['Java', 'C++', 'Python', 'HTML']
'java,python,html,css,javascript'.split(',')
['java', 'python', 'html', 'css', 'javascript']
names = input("Enter names: ").split(',')
Enter names: Asif Amaan Syed Akheel Soha
names
['Asif Amaan Syed Akheel Soha']
names = input("Enter names: ").split(',')
Enter names: Asif, Amaan, Syed, Akheel, Soha
names
['Asif', ' Amaan', ' Syed', ' Akheel', ' Soha']
numbers = input("Enter the numbers ").split()
Enter the numbers 1 2 3 8 9 3 6
numbers
['1', '2', '3', '8', '9', '3', '6']
int(['1', '2', '3', '8', '9', '3', '6'])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(['1', '2', '3', '8', '9', '3', '6'])
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
map(int,['1', '2', '3', '8', '9', '3', '6'])
<map object at 0x0000019746468800>
list(map(int,['1', '2', '3', '8', '9', '3', '6']))
[1, 2, 3, 8, 9, 3, 6]
numbers = list(map(int, input("Enter the nums: ").split()))
Enter the nums: 5 6 7 8 43 17 2004 02
numbers
[5, 6, 7, 8, 43, 17, 2004, 2]
numbers = list(map(float, input("Enter the nums: ").split()))
Enter the nums: 56.9 87.90 54.87 45.32
numbers
[56.9, 87.9, 54.87, 45.32]
numbers = tuple(map(int, input("Enter the numbers: ").split()))
Enter the numbers: 1 4 17 2004 02
numbers
(1, 4, 17, 2004, 2)
numbers = tuple(map(float, input("Enter the numbers: ").split()))
Enter the numbers: 32.9 56 89.7
numbers
(32.9, 56.0, 89.7)
names = tuple(input().split())
asif amaan syed
names
('asif', 'amaan', 'syed')
names = set(input().split())
laptop phone computer
names
{'computer', 'phone', 'laptop'}
numbers = set(map(float, input().split()))
3 4 6.7 5.0
numbers
{3.0, 4.0, 5.0, 6.7}
numbers = set(map(int, input().split()))
4 5 73 56 89
numbers
{4, 5, 73, 56, 89}

a,b,c = list(map(int, input().split()))
1 2 3
a
1
b
2
c
3

email, password = ['@gmail.com', 'pass@123']
email, password = input().split()
sasifamaan17@gmail.com 1702@asif
email
'sasifamaan17@gmail.com'
password
'1702@asif'

a = eval(input())
12
a
12

a = eval(input())
356.98
a
356.98

a = eval(input("Enter the input: "))
Enter the input: 'amaan'
a
'amaan'

a = eval(input("Enter the input "))
Enter the input [1,3, 5, 3, 6]
a
[1, 3, 5, 3, 6]

a = eval(input("Enter the input: "))
Enter the input: (2, 4, 5, 3, 2, 3)
a
(2, 4, 5, 3, 2, 3)

a = eval(input("Enter the input: "))
Enter the input: {2, 4, 6, 5, 2, 4, 6}
a
{2, 4, 5, 6}

a = eval(input("Enter the input: "))
Enter the input: {1:2, 3:5, 8:'amaan'}
a
{1: 2, 3: 5, 8: 'amaan'}

a = eval(input("Enter the input: "))
Enter the input: True
a
True


a,b,c = 17, 92.8, 'amaan'
>>> a
17
>>> b
92.8
>>> c
'amaan'
>>> print(a,b,c)
17 92.8 amaan
>>> print('a =',a, 'b =',b, 'c =',c)
a = 17 b = 92.8 c = amaan
>>> print('a =',a,'b =',b,'c =',c,sep='')
a =17b =92.8c =amaan
>>> print('a =',a,'b =',b,'c =',c,sep='\n')
a =
17
b =
92.8
c =
amaan
>>> print('a =',a,'b =',b,'c =',c,sep='@@')
a =@@17@@b =@@92.8@@c =@@amaan
>>> print('a =',a,'b =',b,'c =',c,sep='@@',end='\n\n')
a =@@17@@b =@@92.8@@c =@@amaan

>>> print('a =',a,'b =',b,'c =',c,sep='@@',end='...........')
a =@@17@@b =@@92.8@@c =@@amaan...........
>>> print(f'a={a} b={b} c={c}')
a=17 b=92.8 c=amaan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=17 b=92.800000 c=amaan
>>> print('a=%d b=%.2f c=%s'%a,b,c))
SyntaxError: unmatched ')'
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=17 b=92.80 c=amaan
>>> print('a={} b={} c={}'.format(a,b,c))
a=17 b=92.8 c=amaan
>>> print('a={} b={} c={}'.format(b,c,a))
a=92.8 b=amaan c=17
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=amaan b=17 c=92.8
