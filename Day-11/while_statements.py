'''i = 20
   while i>9:
        print(i)
        i = i-1
    '''


'''
i = 30
while i<61:
    print(i)
    i += 1
'''


'''
i = 1
while i<11:
    if i == 5:
        break
    print(i)
    i += 1
'''


'''
i=1
while i<11:
    i += 1
    if i == 5:
        continue
    print(i)
'''


'''
i = 1
while i<11:
    if i == 15:
        break
    print(i)
    i += 1
else:
    print('1 to 10 numbers are printed')
'''


a = [1,0,2,4,0,5,2,0,9,0,4,0,0,2,0,0,2,2,4,0]

while 0 in a:
    a.remove(0)

print(a)
