class Redbus:
    bus ={i: "Available" for i in range(1,11)}

    def displayseats(self):
        print("----------xyz bus---------------")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])

    def booking(self,seatno):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i] == 'Available':
                Redbus.bus[i] = 'Booked'
                print(f"Your seat - {seatno} is successfully Bokked")
                break
            else:
                print(f"Your seat - {seatno} is already Booked")

class user(Redbus):
    def __init__(self,name,email,phoneno):
        self.name = name
        self.email = email
        self.phoneno = phoneno
        print(f"Hello {self.name}, Welcome to the RedBus")

shashi = user('shashi','shashi@gmail.com',9876543210)
shashi.displayseats()
shashi.booking(4)
shashi.displayseats()

class Driver(Redbus):
    def __init__(self):
        self.name = 'Pavan'
        self.phno = '9876543210'
        self.__address = 'KPHB'
        self.__email = 'Pavan@gmail.com'
        self.__salary = '30000'
