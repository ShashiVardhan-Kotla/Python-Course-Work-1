from abc import ABC,abstractmethod

class Payment(ABC):
    def source(self):
        print("Scanner/upiid/mobile number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Select the Bank")
    def pin(self):
        print("Enter the pin")

    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment Success/fail")

class HDFC(Payment):
    def paymentprocess(self):
        print("Payment is process through HDFC Bank")

class ICICI(Payment):
    def paymentprocess(self):
        print("Payment is process through ICICI Bank")

class UNION(Payment):
    def paymentprocess(self):
        print("Payment is process through UNION Bank")

class AXIS(Payment):
    def paymentprocess(self):
        print("Payment is process through AXIS Bank")

shashi = HDFC()
shashi.source()
shashi.amount()
shashi.bank()
shashi.pin()
shashi.paymentprocess()
shashi.paymentstatus()

vardhan = ICICI()
vardhan.source()
vardhan.amount()
vardhan.bank()
vardhan.pin()
vardhan.paymentprocess()
vardhan.paymentstatus()

pavan = UNION()
pavan.source()
pavan.amount()
pavan.bank()
pavan.pin()
pavan.paymentprocess()
pavan.paymentstatus()

pranay = AXIS()
pranay.source()
pranay.amount()
pranay.bank()
pranay.pin()
pranay.paymentprocess()
pranay.paymentstatus()