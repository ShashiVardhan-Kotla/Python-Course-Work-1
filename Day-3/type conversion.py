#type conversions
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
(10+0j)bool(a)
SyntaxError: invalid syntax
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
float(a)
10.0
f=13.4
int(f)
13
complex(f)
(13.4+0j)
str(f)
'13.4'
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
str(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    str(c)
NameError: name 'c' is not defined
bool(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    bool(c)
NameError: name 'c' is not defined
list(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list(c)
NameError: name 'c' is not defined
c=12+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> str(c)
'(12+3j)'
>>> bool(c)
True
>>> s="Codegnan"
>>> a="876543"
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'Codegnan'
>>> int(a)
876543
>>> float(a)
876543.0
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'Codegnan'
>>> complex(a)
(876543+0j)
>>> bool(a)
True
>>> list(a)
['8', '7', '6', '5', '4', '3']
>>> list(s)
['C', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
>>> tuple(s)
('C', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
>>> set(s)
{'e', 'd', 'a', 'C', 'n', 'o', 'g'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
