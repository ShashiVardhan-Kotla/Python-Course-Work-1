'''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

shashi = whatsappv1()
shashi.message()

shashi = whatsappv2()
shashi.message()
shashi.status()

class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3(whatsappv2):
    def groups(self):
        print("You can create group and talk with multiple people")
        
shashi = whatsappv1()        
shashi.message()

shashi = whatsappv2()
shashi.message()
shashi.status()

shashi = whatsappv3()
shashi.message()
shashi.status()
shashi.groups()

class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3:
    def groups(self):
        print("You can create group and talk with multiple people")

class whatsappv4:
    def community(self):
        print("You can multiple groups")

class whatsappv5(whatsappv4,whatsappv3,whatsappv2):
    def channels(self):
        print("You can post regularly with huge crowd")

shashi = whatsappv5()
shashi.message()
shashi.status()
shashi.groups()
shashi.community()
shashi.channels()
'''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3(whatsappv1):
    def groups(self):
        print("You can create group and talk with multiple people")

shashi =whatsappv3()
shashi.message()
shashi.groups()

