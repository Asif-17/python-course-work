'''
try:
    # n += 10
    a = int(input("Enter the integer: "))
    
    l=[1,2,3,3,4]
    # print(l[10])

    k = {1:1,2:4,3:9,4:16}
    # print(k[9])

    # c=12/0
    # m=10 + 'a'


except NameError:
    print("Variable is not defined")
except ValueError:
    print("Enter the correct datatype")
except IndexError:
    print("Index is out of range")
except KeyError:
    print("Key is not found")
except ZeroDivisionError:
    print("Can't divide with zero")
except TypeError:
    print("Can't add 2 diff datatypes")
    
else:
    print("No Error")
finally:
    print("End of the programming")
'''

'''
try:
    # n += 10
    a = int(input("Enter the integer: "))
    
    l=[1,2,3,3,4]
    # print(l[10])

    k = {1:1,2:4,3:9,4:16}
    # print(k[9])

    # c=12/0
    # m=10 + 'a'


except (NameError, ValueError, IndexError, KeyError, ZeroDivisionError, TypeError) as e:
    print(f'Error Occured: {e}')
else:
    print("No Error")
finally:
    print("End of the programming")
'''

'''
try:
    # n += 10
    a = int(input("Enter the integer: "))
    
    l=[1,2,3,3,4]
    # print(l[10])

    k = {1:1,2:4,3:9,4:16}
    # print(k[9])

    # c=12/0
    # m=10 + 'a'


except Exception as e:
    print(f'Error Occured: {e}')
else:
    print("No Error")
finally:
    print("End of the programming")
'''



try:
    balance = 5000
    withdraw = -6000
    if withdraw<0:
        raise Exception("Please enter positive number")


except Exception as e:
    print(f'Error Occured: {e}')
else:
    print("No Error")
finally:
    print("End of the programming")
