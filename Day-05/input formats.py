Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#input formating
a=input()
codegnan
a
'codegnan'
a=input()
1234
a
'1234'
a=input("enter the value:")
enter the value:jihfhugefewjdjkqwdb
a
'jihfhugefewjdjkqwdb'
marks=input("enter the marks:")
enter the marks:12
marks
'12'
marks=int(input("enter the marks:"))
enter the marks:12
marks
12
price=float(input("enter the price:"))
enter the price:123.45
price
123.45
cgpa=float(input("enterv the cgpa:"))
enterv the cgpa:8.0
cgpa
8.0
names.split
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names.split
NameError: name 'names' is not defined
names.split()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
name=input()
['shashi','vardhan','reddy',ArithmeticError]
['shashi','vardhan','reddy']
['shashi', 'vardhan', 'reddy']
name=
SyntaxError: invalid syntax
name='shashi', 'vardhan', 'reddy'
names.split('-')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names.split('-')
NameError: name 'names' is not defined. Did you mean: 'name'?
course="python-java-c++"
courses.split()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    courses.split()
NameError: name 'courses' is not defined. Did you mean: 'course'?
courses.split("-")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    courses.split("-")
NameError: name 'courses' is not defined. Did you mean: 'course'?
courses.split('-')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    courses.split('-')
NameError: name 'courses' is not defined. Did you mean: 'course'?
courses='python-java-c++'
courses.split('-')
['python', 'java', 'c++']
softskills='communication quicklearner'
softskills.split()
['communication', 'quicklearner']
name=input("enter the names:").split()
enter the names:shashi vardhan reddy
name
['shashi', 'vardhan', 'reddy']
names=tuple(input("enter the name:").split())
enter the name:shashi vardhan reddy
names
('shashi', 'vardhan', 'reddy')
marks=input().split()
12 34 68 89 09
marks
['12', '34', '68', '89', '09']
map(int,marks)
<map object at 0x000001EC14C95C90>
list(map(int,marks))
[12, 34, 68, 89, 9]
marks=list(map(int,input("enter the marks").split()))
enter the marks 12 56 234 67 345 8 345 78
marks
[12, 56, 234, 67, 345, 8, 345, 78]
marks=tuple(map(int,input("enter the marks").split()))
enter the marks 345 456 5678
marks
(345, 456, 5678)
marks=set(map(int,input("enter the marks").split()))
enter the marks 4567 5678 45678
marks
{45678, 5678, 4567}
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,"str")
a
1
b
12.3
c
'str'
email,password=input("enter the email,password:").split()
enter the email,password:reddy@codegnan.com2358
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    email,password=input("enter the email,password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
enter the email, password: reddy@codegnan.com 2358
SyntaxError: invalid syntax
enter email,password:reddy@codegnan.com2358
SyntaxError: invalid syntax
email,password=input('enter the email,password:').split()
enter the email,password:reddy@codegnan.com2358
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    email,password=input('enter the email,password:').split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password=input('enter the email, password:').split()
enter the email, password:reddy@codegnan.com 2345
>>> email
'reddy@codegnan.com'
>>> password
'2345'
>>> a,b,c=list(map(int,input().split()))
30,20,10
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: '30,20,10'
>>> 30 20 10
SyntaxError: invalid syntax
>>> a
1
>>> 30 20 10
SyntaxError: invalid syntax
>>> a,b,c=list(map(int,input().split()))
... 10 20 30
SyntaxError: multiple statements found while compiling a single statement
>>> a,b,c=list(map(int,input().split(',')))
10,20,30
>>> a,b,c
(10, 20, 30)
>>> status=eval(input())
12
>>> status
12
>>> type(status)
<class 'int'>
>>> status=eval(input())
3+8j
>>> status
(3+8j)
>>> type(status)
<class 'complex'>
>>> <class 'complex'>
SyntaxError: invalid syntax
>>> status=eval(input())
20.33
>>> type(status)
<class 'float'>
>>> d=eval(input())
{'name':'bunny','age':20}
>>> d
{'name': 'bunny', 'age': 20}
