# products = ['laptop', 'TV', 'phone', 'smartwatch']

# a = 'laptop'

# for i in products:
#     if i == a:
#         print(i)
#         break
# else:
#     print("Not Found")
    


pin = 12345

for i in range(5):
    epin = int(input("Enter the pin: "))
    if pin == epin:
        print("Login successful")
        break
    else:
        print("Incorrect pin")
else:
    print("Try again after 60 seconds")
