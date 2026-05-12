# open close write read append

# file = open("file_operation.txt",'r')
'''
print(file.read())
file.close()
'''

'''
print(file.readlines())
file.close()
'''

'''
print(file.readline())
file.close()
'''

'''
print(file.readline())
print(file.readlines())
print(file.read())
file.close()
'''

'''
print(file.readline())
file.seek(0)
print(file.readlines())
file.seek(0)
print(file.read())
file.close()
'''

'''
with open("file_operation.txt",'r') as file:
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read())
'''

'''
with open("file_operation.txt",'w') as file:
    file.write('Asif, Akheel, Nagaraju, Mehaboob')
'''

'''
with open("file_operation.txt",'a') as file:
    file.write('Friends')
'''


'''
with open("file_operation.txt",'a+') as file:
    file.write('Friends')
    file.seek(0)
    print(file.read())
'''

'''
with open("file_2.txt",'a+') as file:
    file.write('Friends')
    file.seek(0)
    print(file.read())
'''

'''
with open("file_2.txt",'w+') as file:
    file.write('Friends')
    file.seek(0)
    print(file.read())
'''

'''
try:
    with open("file_3.txt",'r+') as file:
        file.write('Friends')
        file.seek(0)
        print(file.read())
except Exception as e:
    print("Error Occured: ",e)
'''


try:
    with open('names.txt','w+') as file:
        for i in range(5):
            name = input("Enter the name: ")
            marks = int(input("Enter the marks: "))
            file.write(f"{name}: {marks}")

        file.seek(0)
        print(file.read())
except Exception as e:
    print("Error Occured:",e)
