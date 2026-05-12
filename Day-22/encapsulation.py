'''
class Instagram:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email      #public
        self.__password = password     #private

asif = Instagram('Asif','sasifamaan17@gmail.com','Asif@1980')

print('Username: ', asif.username)
print('Email: ', asif._email)
print('Password: ', asif.__password)
'''


class Instagram:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email      
        self.__password = password

    @property
    def emailaccess(self):
        return self._email

    @emailaccess.setter
    def emailaccess(self,new_email):
        self._email = new_email

    def getpassword(self):
        return self.__password

    def setpassword(self,new_password):
        self.__password = new_password

asif = Instagram('Asif','sasifamaan17@gmail.com','Asif@1980')

print('Before Username: ', asif.username)
asif.username = 'Amaan'
print('After Username: ', asif.username)

print('Before Email: ', asif.emailaccess)
asif.emailaccess = 'asifamaan1702@gmail.com'
print('After Email: ', asif.emailaccess)

print('Before Password: ', asif.getpassword())
asif.setpassword('amaan@290')
print('After Password: ', asif.getpassword())
