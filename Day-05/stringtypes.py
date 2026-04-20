Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='amaan'
s
'amaan'
type(s)
<class 'str'>
fname = 'asif'
lname = 'amaan'
fname + lname
'asifamaan'
lname = ' amaan'
fname + lname
'asif amaan'
fname*4
'asifasifasifasif'
fname*17
'asifasifasifasifasifasifasifasifasifasifasifasifasifasifasifasifasif'


s='python'
s[4]
'o'
s[5]
'n'
s[9]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[9]
IndexError: string index out of range
s[-1]
'n'
s[-4]
't'

names = 'asif amaan soha syed aamina'
names
'asif amaan soha syed aamina'
names[0]
'a'
names[4]
' '
names[-7]
' '
names[-9]
'e'
names[-16]
's'
names[-27]
'a'
names[28]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    names[28]
IndexError: string index out of range
names[26]
'a'


names[0:4]
'asif'
names[6:11]
'maan '
names[5:11]
'amaan '
names[12:16]
'oha '
names[11:16]
'soha '
names[16:21]
'syed '
names[21:]
'aamina'
names[:15]
'asif amaan soha'
names[::2]
'ai ma oase aia'
names[-1:-7]
''
names[-6:]
'aamina'
names[-1:-7:-1]
'animaa'
names[-6:-14:-1]
'a deys a'
names[::-1]
'animaa deys ahos naama fisa'
 names
 
SyntaxError: unexpected indent
names
'asif amaan soha syed aamina'
names[-22:-17]
'amaan'
asif in names
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    asif in names
NameError: name 'asif' is not defined. Did you mean: 'ascii'?
'asif' in names
True
'soha' in names
True
'sana' in names
False
'syed' not in names
False


len(names)
27
sorted(names)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'd', 'e', 'f', 'h', 'i', 'i', 'm', 'm', 'n', 'n', 'o', 's', 's', 's', 'y']
max(names)
'y'
min(names)
' '
ord('a')
97
ord('A')
65
ord(' ')
32
ord('17')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    ord('17')
TypeError: ord() expected a character, but string of length 2 found
ord('4')
52
chr(17)
'\x11'
chr(97)
'a'
chr(100)
'd'
ord('&')
38
ord('+')
43
chr(112)
'p'
chr(128)
'\x80'
chr(127)
'\x7f'
chr(129)
'\x81'



names
'asif amaan soha syed aamina'
names.upper()
'ASIF AMAAN SOHA SYED AAMINA'
names.lower()
'asif amaan soha syed aamina'
names.capitalize()
'Asif amaan soha syed aamina'
names.title()
'Asif Amaan Soha Syed Aamina'
names = 'Asif Amaan Soha Syed Aamina'
names
'Asif Amaan Soha Syed Aamina'
names.swapcase()
'aSIF aMAAN sOHA sYED aAMINA'
names.casefold()
'asif amaan soha syed aamina'
names.center(50,'*')
'***********Asif Amaan Soha Syed Aamina************'
names.center(70,'-')
'---------------------Asif Amaan Soha Syed Aamina----------------------'
names.ljust(70,'-')
'Asif Amaan Soha Syed Aamina-------------------------------------------'
names.rjust(70,'-')
'-------------------------------------------Asif Amaan Soha Syed Aamina'


num = '654321'
num.zfill(10)
'0000654321'
num.zfill(7)
'0654321'
num.zfill(5)
'654321'
num.zfill(15)
'000000000654321'


names
'Asif Amaan Soha Syed Aamina'
names.find('Asif')
0
names.find('Soha')
11
names.find('S')
11
names.find('A')
0
names.find('n')
9
names.find('u')
-1
names.find('D')
-1
names.rfind('A')
21
names.index('a')
7
names.rindex('a')
26
names.index('u')
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    names.index('u')
ValueError: substring not found
names.count('a')
5
names.count('A')
3
names.count('U')
0


names
'Asif Amaan Soha Syed Aamina'
names.replace('a', '*')
'Asif Am**n Soh* Syed A*min*'
names.replace('A', '0')
'0sif 0maan Soha Syed 0amina'
names.replace('Syed', 'Farheen')
'Asif Amaan Soha Farheen Aamina'
names.replace('Haneef', 'Mohammad')
'Asif Amaan Soha Syed Aamina'
names.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
names.translate(names.maketrans('aeiou', '12345'))
'As3f Am11n S4h1 Sy2d A1m3n1'


names
'Asif Amaan Soha Syed Aamina'
names.split()
['Asif', 'Amaan', 'Soha', 'Syed', 'Aamina']
names.split(' ',3)
['Asif', 'Amaan', 'Soha', 'Syed Aamina']
names.rsplit(' ', 3)
['Asif Amaan', 'Soha', 'Syed', 'Aamina']

s = 'python\nprogramming\nlang'
s
'python\nprogramming\nlang'
s.splitlines()
['python', 'programming', 'lang']

l = ['python', 'programming', 'lang']
','.join(l)
'python,programming,lang'
>>> n = ['Asif', 'Amaan', 'Soha', 'Syed', 'Aamina']
>>> '@'.join(n)
'Asif@Amaan@Soha@Syed@Aamina'
>>> 
>>> names
'Asif Amaan Soha Syed Aamina'
>>> names.partition(' ')
('Asif', ' ', 'Amaan Soha Syed Aamina')
>>> names.partition('a')
('Asif Am', 'a', 'an Soha Syed Aamina')
>>> names.rpartition('a')
('Asif Amaan Soha Syed Aamin', 'a', '')
>>> 'abcbc'.partition('b')
('a', 'b', 'cbc')
>>> 'abcbc'.rpartition('b')
('abc', 'b', 'c')
>>> 
>>> 
>>> s = '          hello      world     '
>>> s.split()
['hello', 'world']
>>> s.strip()
'hello      world'
>>> s.lstrip()
'hello      world     '
>>> s.rstrip()
'          hello      world'
>>> s.replace(' ','')
'helloworld'
>>>  y = 'Asif is doing Python Coding $%*'
...  
SyntaxError: unexpected indent
>>> y = 'Asif is doing Python Coding $%*'
>>> y.encode()
b'Asif is doing Python Coding $%*'
>>> y = 'भबटग Āá'
>>> y.encode()
b'\xe0\xa4\xad\xe0\xa4\xac\xe0\xa4\x9f\xe0\xa4\x97 \xc4\x80\xc3\xa1'
>>> b'\xe0\xa4\xad\xe0\xa4\xac\xe0\xa4\x9f\xe0\xa4\x97 \xc4\x80\xc3\xa1'.decode()
'भबटग Āá'
