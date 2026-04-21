Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> d = {}
>>> d = dict()
>>> type(d)
<class 'dict'>
>>> d = {'name':'asif', 'course':'python', 'batch':52}
>>> d
{'name': 'asif', 'course': 'python', 'batch': 52}
>>> d['name']='amaan'
>>> d
{'name': 'amaan', 'course': 'python', 'batch': 52}
>>> d['skills'] = ['python, 'html', 'css']
...                
SyntaxError: unterminated string literal (detected at line 1)
>>> d['skills'] = 'ai ml'
...                
>>> d
...                
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml'}
>>> 
>>> 
>>> s = {}
...                
>>> s[1] = 'int'
...                
>>> s[1.2] = 'float'
...                
>>> s
...                
{1: 'int', 1.2: 'float'}
>>> s[(1,2,3)] = 'tuple'
...                
>>> s
...                
{1: 'int', 1.2: 'float', (1, 2, 3): 'tuple'}
>>> s[{1,2,3}] = 'set'
...                
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s[{1,2,3}] = 'set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
s[False] = 1
               
s
               
{1: 'int', 1.2: 'float', (1, 2, 3): 'tuple', False: 1}


d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml'}
d['name']
               
'amaan'
d['course']
               
'python'
d['age']
               
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d['age']
KeyError: 'age'

d.get('name')
               
'amaan'
d.get('age')
               
d.get('age', 'age is not present')
               
'age is not present'
d.get('name', 'name is not present')
               
'amaan'

'course' in d
               
True
'amaan' in d
               
False


d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml'}
d['institute']='Codegnan'
               
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan'}
d['age']=22
               
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan', 'age': 22}
d.update({'location':'JNTU', 'city':'Hyderabad'})
               
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan', 'age': 22, 'location': 'JNTU', 'city': 'Hyderabad'}


d.popitem()
               
('city', 'Hyderabad')
d.popitem()
               
('location', 'JNTU')
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan', 'age': 22}
d.pop('skills')
               
'ai ml'
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'institute': 'Codegnan', 'age': 22}
del d['age']
               
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'institute': 'Codegnan'}
d.clear()
               
d
               
{}


d = {'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan', 'age': 22, 'location': 'JNTU', 'city': 'Hyderabad'}
               
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan', 'age': 22, 'location': 'JNTU', 'city': 'Hyderabad'}
d.keys()
               
dict_keys(['name', 'course', 'batch', 'skills', 'institute', 'age', 'location', 'city'])
d.values()
               
dict_values(['amaan', 'python', 52, 'ai ml', 'Codegnan', 22, 'JNTU', 'Hyderabad'])
d.items()
               
dict_items([('name', 'amaan'), ('course', 'python'), ('batch', 52), ('skills', 'ai ml'), ('institute', 'Codegnan'), ('age', 22), ('location', 'JNTU'), ('city', 'Hyderabad')])
sorted(d)
               
['age', 'batch', 'city', 'course', 'institute', 'location', 'name', 'skills']
len(d)
               
8
max(d)
               
'skills'
min(d)
               
'age'


d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan', 'age': 22, 'location': 'JNTU', 'city': 'Hyderabad'}
d.get('key')
               
d.setdefault('key','value')
               
'value'
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan', 'age': 22, 'location': 'JNTU', 'city': 'Hyderabad', 'key': 'value'}
d.get('city')
               
'Hyderabad'
d.setdefault('city', 'Kurnool')
               
'Hyderabad'
d
               
{'name': 'amaan', 'course': 'python', 'batch': 52, 'skills': 'ai ml', 'institute': 'Codegnan', 'age': 22, 'location': 'JNTU', 'city': 'Hyderabad', 'key': 'value'}
