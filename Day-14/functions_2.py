# mutable - changes reflecting in and out - pass by reference (list, set, dict)
# immutable - changes reflecting only inside - pass by value (int, float, str, tuple, bool)


'''
def display(n):
    n += 20
    print("Inside: ", n)

n=10
display(n)
print("Outside: ", n)
'''


'''
def display(n):
    n += ' Amaan'
    print("Inside: ", n)

n= 'Asif'
display(n)
print("Outside: ", n)
'''


'''
def display(n):
    n.extend([6,8,5])
    print("Inside: ", n)

n= [1,2,3,9]
display(n)
print("Outside: ", n)
'''

'''
def display(n):
    n.add(6)
    print("Inside: ", n)

n= {1,2,3,9}
display(n)
print("Outside: ", n)
'''

'''
def display(n):
    n[5]=5
    print("Inside: ", n)

n= {1:1,2:2,3:3,4:4}
display(n)
print("Outside: ", n)
'''

'''
def display(n):
    n = False
    print("Inside: ", n)

n= True
display(n)
print("Outside: ", n)
'''

'''
# Global scope Keyword/variable

def display():
    global n
    n += 20
    print("Inside: ", n)

n=10
display()
print("Outside: ", n)
'''

'''
def display():
    global n
    n = 20
    print("Inside: ", n)

display()
print("Outside: ", n)
'''


'''
# Nonlocal variable

def display(course):
    print("Starting: ",course)
    def change():
        nonlocal course
        course = 'JFS'
        print("Course changed: ", course)
    change()
    print("Final: ", course)

course = 'PFS'
display(course)
'''

'''
s = 'Python'
print(len(s))

len = 23
print(len(s))
'''


