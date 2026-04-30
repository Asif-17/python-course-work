'''
password = input("Enter the password: ")

if len(password) >= 8:
    status = set()
    for i in password:
        if i.isupper():
            status.add('u')
        elif i.islower():
            status.add('l')
        elif i.isdigit():
            status.add('d')
        else:
            status.add('s')
    if len(status) == 4:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")
'''


'''
products = {
    'Rice':60, 'Wheat Flour':45, 'Sugar':40, 'Milk':25, 'Eggs (12 pcs)':70, 'Cooking Oil':130, 'Tea Powder':90, 'Salt':20, 'Bread':30, 'Soap':25
    }

for i in enumerate(products):
    print(i[0], i[1], products[i[1]])
    '''

products = {
    1:{'name':'Rice','Price':60},
    2:{'name':'Wheat Flour', 'Price':45},
    3:{'name':'Sugar', 'Price':40},
    4:{'name':'Milk', 'Price':25},
    5:{'name':'Eggs', 'Price':70},
    6:{'name':'Cooking Oil', 'Price':130},
    7:{'name':'Tea powder', 'Price':90},
    8:{'name':'Salt', 'Price':20},
    9.{'name':'Bread', 'Price':30},
    10.{'name':'Soap', 'Price':25},
}

print('------ Welcome to Supermarket ------')
print('Here are the products which are available: ')

print('Index'.ljust(5,' '), 'Product'.ljust(20,' '), 'Price (Rs.)')

for i in products:
    print(str(i).ljust(5,' '), products[i]['name'].ljust(20,' '), products[i].['Price'])


