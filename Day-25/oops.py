'''
class Flipkart:
    discount = 30
    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the Flipkart',self.name)

shashi = Flipkart()
shashi.info('shashi',9876543210,'Hyd')
pavan = Flipkart()
pavan.info('pavan',9876543210,'Blr')
pranay = Flipkart()
pranay.info('pranay',9876543210,'Vij')
'''
class Flipkart:
    discount = 30

    classmethod
    def updatediscount(cls):
        cls.discount = 40
        print("Updated Discount:",cls.discount)

    def info(self,name,phoneno,address):
            self.name = name
            self.phoneno = phoneno
            self.address = address
            print(f'Welcome to the Flipkart',self.name)

    @staticmethod
    def banner():
         print(f"{Flipkart.discount}% discount is going, grab the products------")

shashi = Flipkart()
shashi.info('shashi',9876543210,'Hyd')
shashi.updatediscount()
shashi.banner()

pavan = Flipkart()
pavan.info('pavan',9876543210,'Blr')
pavan.updatediscount()
pavan.banner()

pranay = Flipkart()
pranay.info('pranay',9876543210,'Vij')
pranay.updatediscount()
pranay.banner()