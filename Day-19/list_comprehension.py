Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
res = [i for i in range(1,11)]
res
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i*2 for i in range(1,11)]
res
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
res = [i+10 for i in range(1,11)]
res
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> 
>>> 
>>> res = [i for i in range(10,101,10)]
>>> res
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> res = [i for i in range(10,101,10) if i%20==0]
>>> res
[20, 40, 60, 80, 100]
>>> 
>>> 
>>> res = [i if i%2==0 else 0 for i in range(1,21)]
>>> res
[0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16, 0, 18, 0, 20]
>>> 
>>> 
>>> s = 'Python Progamming Language'
>>> vol = 'aeiouAEIOU'
>>> res = [i for i in s]
>>> res
['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'L', 'a', 'n', 'g', 'u', 'a', 'g', 'e']
>>> res = ['*' if i in vol else i for i in s]
>>> res
['P', 'y', 't', 'h', '*', 'n', ' ', 'P', 'r', '*', 'g', '*', 'm', 'm', '*', 'n', 'g', ' ', 'L', '*', 'n', 'g', '*', '*', 'g', '*']
>>> ''.join(res)
'Pyth*n Pr*g*mm*ng L*ng**g*'
>>> ' '.join(res)
'P y t h * n   P r * g * m m * n g   L * n g * * g *'
>>> 
>>> 
>>> 
>>> s = {i for i in range(7,71,7)}
>>> s
{35, 70, 7, 42, 14, 49, 21, 56, 28, 63}
>>> 
>>> 
>>> 
>>> s = {i:i*7 for i in range(1,11)}
>>> s
{1: 7, 2: 14, 3: 21, 4: 28, 5: 35, 6: 42, 7: 49, 8: 56, 9: 63, 10: 70}
