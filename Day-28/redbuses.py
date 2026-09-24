class redbus:
    bus = {i: "Available" for i in range(1,11)}

    def displayseats(self):
        print("---------xyz bus-----------")
        for i in redbus.bus:
            print(i,redbus.bus[i])

    def booking(self,seatno):
        for i in redbus.bus:
            if i == seatno and redbus.bus[i] == 'Available':
                redbus.bus[i] = 'Booked'
                print(f"Your seat - {seatno} is successfully Booked")
                break
            else:
                print(f"Your seat - {seatno} is already Booked")

class User(redbus):
    def __init__(self,name,email,phoneno):
        self.name = name
        self.email = email
        self.phoneno = phoneno
        print(f"Hello {self.name}, Welcome to the redbus")

Shashi = User('Shashi','Shashi@gmail.com',9876543210)
Shashi.displayseats()
Shashi.booking(6)
Shashi.displayseats()
Shashi.booking(6)
