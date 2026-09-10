'''
def functionname(arg):
    #stsmt
    return (opt)
functionname(para)

def gst(price):
    print("Original Price:",price)
    print("Final Price:",price+price*0.18)

gst(1000)
gst(5000)
gst(800)
gst(500)
gst(10000)


def table(n):
    print(f'{n}*{i}={n*i}')
    print('--------------------')
    for i in range(1,11):
        print(f'{n}*{i}={n*i}')

for i in range(1,21):
    table(i) 

def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

    print(isleap(2012))
    print(isleap(2020))
    print(isleap(2026))

def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "Not a Prime number"

    return "Prime Number"
print(isprime(16))
print(isprime(17))
print(isprime(18))
print(isprime(19))

def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display('vardhan','vardhan@gmail.com','vardhan@123')
display('vardhan@gmail.com','vardhan','vardhan@123')
display('vardhan@123','vardhan','vardhan@gmail.com')

def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display(name='vardhan',email='vardhan@gmail.com',pwd='vardhan@123')
display(email='vardhan@gmail.com',name='vardhan',pwd='vardhan@123')
display(pwd='vardhan@123',name='vardhan',email='vardhan@gmail.com')

def display(name,email,pwd=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display("vardhan","email")
display("vardhan","email","pwd@123")

def display(*names):
    print(names)

display("vardhan")
display("vardhan","pavan")
display("vardhan","pavan","pranay")
display("vardhan","pavan","pranay","karthik")
'''
def display(**names):
    print(names)

display(n1="vardhan")
display(n1="vardhan",n2="pavan")
