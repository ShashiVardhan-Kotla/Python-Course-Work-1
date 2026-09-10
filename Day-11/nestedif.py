'''
fa = eval(input("Follows Account: "))
if fa:
    cf = eval(input("Close Friend: "))
    if cf:
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account First")

reg = eval(input("Registered: "))
if reg:
    fee = eval(input("Fee Paid: "))
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")    
'''
data ={
    'prasad':{'status':True,'python':90,'mysql':95,'flask':98},
    'dipak':{'status':False,'python':None,'mysql':None,'flask':None},
    'teja':{'status':True,'python':20,'mysql':35,'flask':38},
    'dinesh':{'status':True,'python':60,'mysql':65,'flask':70},
    'nikhil':{'status':True,'python':70,'mysql':75,'flask':75},
    'vardhan':{'status':True,'python':75,'mysql':65,'flask':80},
}
name = input("Enter name:")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg = sum/3
        print("hello {name}!!!")
        print("your average score is {avg}")
        if avg >=90:
            print("Outstanding")
        if avg >=80:
            print("very good")
        if avg >=70:
            print("good")
        if avg >=35:
            print("Better luck next time")
        else:
            print("failed")
    else:
        print(f'{name} did not attend the exam')
else:
    print("Absent")                                