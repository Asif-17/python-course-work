data = {
    12345:{'pin':1234,'balance':7000,'history':[]},
    34675:{'pin':2345,'balance':9000,'history':[]},
    56743:{'pin':3456,'balance':8000,'history':[]},
    74976:{'pin':3456,'balance':5000,'history':[]},
}
acc_num = None

def login(e_num,e_pin):
    if e_num in data and data[e_num]['pin']==e_pin:
        print("Login Successful")
        global acc_num
        acc_num = e_num
        return True
    else:
        print("Invalid Login")
        return False


def check_balance():
    print("Current Balance",data[acc_num]['balance'])

def deposit():
    amount = int(input("Enter the deposit amount: "))
    data[acc_num]['balance'] += amount
    data[acc_num]['history'].append(f'{amount} is deposited ++++')
    print('Deposit Successful')

def withdraw():
    amount = int(input("Enter the withdraw amount: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        data[acc_num]['history'].append(f'{amount} is withdraw ----')
        print('Withdraw Succcessful')
    else:
        print('Insufficient Balance')

def viewtransaction():
    if data[acc_num]['history']:
        print("----------Transactions History----------")
        for i in data[acc_num]['history']:
            print(i)
        print("----------End of the history----------")
    else:
        print("No Transaction")
