# Recursions - Function calling itself

'''
def display(n):
    if n>15:
        return

    print(n)
    display(n+1)

display(1)
'''


'''
def display(n):
    if n<1:
        return

    print(n)
    display(n-1)

display(10)
'''


'''
def display(n):
    if n>15:
        return

    display(n+1)
    print(n)

display(1)
'''


'''
def display(n,sum):
    if n>15:
        return sum
    return display(n+1, sum+n)
print(display(1,0))
'''

'''
def display(n,sum):
    if n>10:
        return sum
    return display(n+1, sum*n)
print(display(1,1))
'''

'''
def display(i,s):
    if i==len(s):
        return
    print(s[i])
    return display(i+1,s)

s = "Asif Amaan"
display(0,s)
'''

'''
def display(i,s):
    if i==len(s):
        return
    
    display(i+1,s)
    print(s[i])

s = "Asif Amaan"
display(0,s)
'''

'''
def display(i,s):
    if i==len(s):
        return
    print(s[:i+1])
    return display(i+1,s)

s = "Asif Amaan"
display(0,s)
'''

'''
def display(i,s):
    if i==len(s):
        return
    
    display(i+1,s)
    print(s[:i+1])

s = "Asif Amaan"
display(0,s)
'''

'''
def display(i,s):
    if i==len(s):
        return
    print(s[i:i+3])
    return display(i+1,s)

s = "Asif Amaan"
display(0,s)
'''

'''
def display(i):
    if i==len(s):
        return
    print(s[i:i+5])
    return display(i+1)

s = "Asif Amaan"
display(0)
'''

# Factorial
'''
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
print(factorial(8))
'''

'''
def display(n):
    if n==0:
        return
    print(n%10)
    display(n//10)

display(12345)
'''


'''
def display(n):
    if n==0:
        return 0
    return (n%10) + display(n//10)

print(display(12345))
'''


