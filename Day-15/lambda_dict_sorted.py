Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> d = {'soha':67, 'amaan':78, 'sameer':43, 'asif':98, 'syed':65}
>>> d
{'soha': 67, 'amaan': 78, 'sameer': 43, 'asif': 98, 'syed': 65}
>>> sorted(d)
['amaan', 'asif', 'sameer', 'soha', 'syed']
>>> sorted(d.items())
[('amaan', 78), ('asif', 98), ('sameer', 43), ('soha', 67), ('syed', 65)]
>>> dict(sorted(d.items()))
{'amaan': 78, 'asif': 98, 'sameer': 43, 'soha': 67, 'syed': 65}
>>> dict(sorted(d.items(),reverse=True))
{'syed': 65, 'soha': 67, 'sameer': 43, 'asif': 98, 'amaan': 78}
>>> dict(sorted(d.items(),key=lambda i:i[1]))
{'sameer': 43, 'syed': 65, 'soha': 67, 'amaan': 78, 'asif': 98}
>>> dict(sorted(d.items(),key=lambda i:i[1],reverse=True))
{'asif': 98, 'amaan': 78, 'soha': 67, 'syed': 65, 'sameer': 43}
