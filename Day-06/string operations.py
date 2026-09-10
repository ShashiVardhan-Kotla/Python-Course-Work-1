Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#how to declare str
s="codegnan"
s
'codegnan'
type(s)
<class 'str'>
s=" "
s
' '
a='python'
b='programming'
a+b
'pythonprogramming'
fname=Shashi Vardhan
SyntaxError: invalid syntax
'*'*20
'********************'
'-codegnan-'*5
'-codegnan--codegnan--codegnan--codegnan--codegnan-'
names = 'shashi deepak dinesh prasad nikhil bunny'
names
'shashi deepak dinesh prasad nikhil bunny'
names[:6]
'shashi'
names[7:13]
'deepak'
names[14:20]
'dinesh'
names[15:21]
'inesh '
names[21:27]
'prasad'
names[28:34]
'nikhil'
names[-1:-5]
''
names[-5]
'b'
names[:-5]
'shashi deepak dinesh prasad nikhil '
names[-5:]
'bunny'
names[::-1]
'ynnub lihkin dasarp hsenid kapeed ihsahs'
names
'shashi deepak dinesh prasad nikhil bunny'
'shashi' in names
True
'prasad' in names
True
'deppak' in names
False
'deepak' in names
True
'teja' in names
False
len (names)
40
ord('a')
97
ord('v')
118
ord('a')
97
ord('g')
103
chr(100)
'd'
chr(40)
'('
chr(10)
'\n'
sorted(names)_
SyntaxError: invalid syntax
sorted(names)
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'b', 'd', 'd', 'd', 'e', 'e', 'e', 'h', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'k', 'k', 'l', 'n', 'n', 'n', 'n', 'p', 'p', 'r', 's', 's', 's', 's', 'u', 'y']
max(names)
'y'
min(names)
' '
s='python Programming language'
s.upper()
'PYTHON PROGRAMMING LANGUAGE'
s.lower()
'python programming language'
s.swapcase()
'PYTHON pROGRAMMING LANGUAGE'
s.capitalize()
'Python programming language'
s.title()
'Python Programming Language'
s
'python Programming language'
s.center(50,'-')
'-----------python Programming language------------'
s.center(50,'*')
'***********python Programming language************'
s.center(40,'.')
'......python Programming language.......'
>>> s.ljust(40,'.')
'python Programming language.............'
>>> s.rjust(40,'.')
'.............python Programming language'
>>> '123'.zfill(4)
'0123'
>>> s.find('g')
10
>>> s.find('p')
0
>>> s.rfind('g')
25
>>> s.rfind('a')
24
>>> s.find('z')
-1
>>> s.find('a')
12
>>> s.index('a')
12
>>> s.rindex('a')
24
>>> s.count('a')
3
>>> s.count('e')
1
>>> s.count('m')
2
>>> s
'python Programming language'
>>>  s.replace('m','2')
...  
SyntaxError: unexpected indent
>>> s.replace('m','2')
'python Progra22ing language'
>>> s.replace('python','java')
'java Programming language'
>>> s.marketrans('aeiou','#@$&*')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.marketrans('aeiou','#@$&*')
AttributeError: 'str' object has no attribute 'marketrans'. Did you mean: 'maketrans'?
>>> s.maketrans('aeiou','#@$&*')
{97: 35, 101: 64, 105: 36, 111: 38, 117: 42}
>>> s.translate(s.maketrans('aeiou','#@$&*')
