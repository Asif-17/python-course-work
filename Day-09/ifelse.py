'''battery = int(input("Enter the phone battery: "))
   if battery <= 18:
        print("Charge the phone or Power Saving Mode")
'''

'''
products = {
    1:{'name':'laptop', 'discount':45},
    2:{'name':'iphone', 'discount':20},
    3:{'name':'smartwatch', 'discount':0},
    4:{'name':'TV', 'discount':65}
    }
print(products)

index = int(input("Enter the index: "))
if products[index]['discount']:
    print(f'{products[index]["name"]} has discount')
'''

'''
technical_skills = {'Python', 'HTML', 'Javascript', 'CSS', 'Flask'}

skills = set(input("Enter your skills: ").split())

if technical_skills == skills:
    print("Congratulations! Your resume is shortlisted")
else:
    print(f"Sorry, you need this skills set: {technical_skills-skills}")
'''

'''
plan = True
if plan:
    print("Ads won't run. You can watch the video without interruption")
else:
    print("Ads will run. Subscribe to youtube premium")
'''


'''
status = input("Enter the status: ")

if status == 'face':
    print("Unlock the mobile")
else:
    print("Unable to reg face")
    if status == 'password':
        print("Unlock the mobile")
    else:
        print('Incorrect password')
'''


'''
vehicle = int(input("Enter the vehicle: "))
if vehicle == 2:
    print('Your bike is on the way. Please pay $50')
elif vehicle == 3:
    print('Your auto is on the way. Please pay $120')
elif vehicle == 4:
    print('Your cab with ac is on the way. Please pay $300')
elif vehicle == 5:
    print('Your cab non-ac is on the way. Please pay $240')
else:
    print('Vehicle not found. Try another vehicle')
'''



products = {
    1:{'name':'laptop', 'discount':45},
    2:{'name':'iphone', 'discount':20},
    3:{'name':'smartwatch', 'discount':0},
    4:{'name':'TV', 'discount':65}
    }

login_status = True

print(products)
order_id = int(input("Enter the index to order: "))

if login_status
