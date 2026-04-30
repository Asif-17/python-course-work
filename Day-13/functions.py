'''
def function_name(a):
    #stmts
    return something

function_name(parameters)
'''



'''
def wish(name):
    print(f'Good Afternoon {name}!')
    print('Welcome to the python class\n')

wish('Asif')
wish('Amaan')
'''


'''
def iseven(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

iseven(21)
iseven(44)
'''


'''
def iseven(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

print(iseven(21))
print(iseven(44))
'''


'''
def avg(a,b,c):
    return (a+b+c)/3

print(avg(4,5,6))
print(avg(14,35,23))
print(avg(34,22,12))
'''

'''
n = int(input("Enter the number: "))
for i in range(2, n//2 + 1):
    if n%i == 0:
        print("Not prime number")
        break
else:
    print("Prime number")
'''


'''
def isprime(n):
    for i in range(2, n//2 + 1):
        if n%i == 0:
            return False
    else:
        return True

print("Prime number" if isprime(13) else "Not prime")
print("Prime number" if isprime(16) else "Not prime")
print("Prime number" if isprime(89) else "Not prime")
'''


'''
def display(name, email, password):
    print("Name: ", name)
    print("Email: ", email)
    print("Password: ", password)

display('Asif', 'sasifamaan17@gmail.com', 'Asif@1511')
display(email='asifamaan@gmail.com', password='Asif@1552', name='Asif')
'''


'''
def display(name, email, password, phoneno=None):
    print("Name: ", name)
    print("Email: ", email)
    print("Password: ", password)
    print("Phone no: ", phoneno)

display('Asif', 'sasifamaan17@gmail.com', 'Asif@1511')
display('Asif', 'sasifamaan17@gmail.com', 'Asif@1511', '9515590954')
'''

'''
def display(*n):
    print(sum(n))

display(1,2,3,4,5,6)
display(1,2,5)
display(7,8,4,3,2,2)
'''

'''
def display(*n):
    print(n,sum(n))

display(1,2,3,4,5,6)
'''


'''
def display(**n):
    print(n)

display(k1='v1', k2='v2')
display(k1='v1')
display(k1='v1',k2='v2',k3='v3')
'''



