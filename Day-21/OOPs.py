'''
class flipkart:              # Class Attribute
    discount = 10
    products = ["Men's Footwear", "T-shirts", "jeans", "Laptop", "Headphones"]

    @classmethod        #Class method
    def showproducts(cls):
        for i in cls.products:
            print(i)

    @classmethod
    def showdiscount(cls):
        print("Discount: ",cls.discount)


asif = flipkart()

asif.showdiscount()
asif.showproducts()

flipkart.showdiscount()
flipkart.showproducts()
'''


class flipkart:              # Class Attribute
    discount = 10
    products = ["Men's Footwear", "T-shirts", "jeans", "Laptop", "Headphones"]

    @classmethod        #Class method
    def showproducts(cls):
        for i in cls.products:
            print(i)

    @classmethod
    def showdiscount(cls):
        print("Discount: ",cls.discount)

    def userinfo(self,username,phoneno):        #Instance Method
        self.username = username
        self.phoneno = phoneno
        print(f"Welcome to the flipkart {self.username}. Shop now")

    @staticmethod         # Static Method
    def banner():
        print("10% discount is going on")

asif = flipkart()

asif.userinfo("Asif","9515590954")
asif.banner()

asif.showdiscount()
asif.showproducts()

flipkart.showdiscount()
flipkart.showproducts()
