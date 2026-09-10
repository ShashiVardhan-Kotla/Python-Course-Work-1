Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> t = ()
>>> t = tuple()
>>> t = (1,2,3,45)
>>> t
(1, 2, 3, 45)
>>> t = (1)
>>> t
1
>>> t = (1,)
>>> t
(1,)
>>> t =(1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> t = (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},True}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> t = (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
>>> t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
>>> type(t)
<class 'tuple'>
>>> <class 'tuple'>
SyntaxError: invalid syntax
>>> t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
>>> (1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
>>> (1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
>>> t[1]
23.4
>>> t[-1]
True
>>> t[-3]
{1, 2, 3}
>>> t[2]
'str'
>>> t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
>>> t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
>>> 23.4 in t
True
'str' in t
True
True in t
True
False in t
False
t = (12,789,32,13,76,32,453,123,7898,1321,32)
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1321, 32)
sorted(t)
[12, 13, 32, 32, 32, 76, 123, 453, 789, 1321, 7898]
max(t)
7898
min(t)
12
len(t)
11
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1321, 32)
t.index(32)
2
t.count(32)
3
all((1,2,3))
True
any((1,2,3,00,0))
True
all((1,2,3,00,0))
False
t = 1,2,3
a,b,c = t
a
1
b
2
c
3
t = (1,2,3,4,[1,2,3],5)
t[4]
[1, 2, 3]
t[4].append(5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t = (1,2,34,4)
sum(t)
41
s = {}
type(s)
<class 'dict'>
#set operations
s = {}
type(s)
<class 'dict'>
s=set()
type(s)
<class 'set'>
s={1,2,3,4,5,6,134124,124,2345234,312}
s
{1, 2, 3, 4, 5, 6, 134124, 2345234, 312, 124}
s={1,1,1,1,1}
s
{1}
s=set()
s.add(1)
s.add(12.3)
s.add("str")
s
{1, 'str', 12.3}
s.add(false)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.add(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
s.add(False)
0
0
s
{False, 1, 'str', 12.3}
a={1,2,3,4,5}
b={3,5,7,8,9}
2 in a
True
10 not in a
True
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
b - a
{8, 9, 7}
a ^ b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
#{1}{1,2}{1,2,3,5},{1,2,3,4,5},{4,5}{4,5,6}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<=a
True
{1,7,8,9}<=a
False
a>={1,2}
True
m={1,2,3}
n={4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(b)
False
a
{1, 2, 3, 4, 5}
a={12,43,1,7,89,40,23,44}
a
{1, 7, 40, 43, 12, 44, 23, 89}
sorted(a)
[1, 7, 12, 23, 40, 43, 44, 89]
max(a)
89
min(a)
1
len(a)
8
a.index(a)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
all({1,1,23,43,13,1})
True
amy({0,''})
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    amy({0,''})
NameError: name 'amy' is not defined. Did you mean: 'any'?
any({0,''})
False
any({0,'',(),True})
True
a
{1, 7, 40, 43, 12, 44, 23, 89}
a={1,2,3}
b=a
b.add(4)
a
{1, 2, 3, 4}
b
{1, 2, 3, 4}
c=a.copy()
c
{1, 2, 3, 4}
c.add(5)
c
{1, 2, 3, 4, 5}
a
{1, 2, 3, 4}
a.add(5)
a
{1, 2, 3, 4, 5}
a.add(100)
a
{1, 2, 3, 4, 5, 100}
a.add(101)
a
{1, 2, 3, 4, 5, 100, 101}
a.update({10,20,30,40})
a
{1, 2, 3, 4, 5, 100, 101, 40, 10, 20, 30}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 100, 101, 40, 10, 20, 30}
a.pop()
3
a.pop()
4
a
{5, 100, 101, 40, 10, 20, 30}
a.remove(101)
a
{5, 100, 40, 10, 20, 30}
a.remove(100)
a
{5, 40, 10, 20, 30}
a.discard(100)
a.discard(30)
a
{5, 40, 10, 20}
a.discard(30)
a
{5, 40, 10, 20}
a.clear()
a
set()
a=frozenset({1,2,3,4})
a
frozenset({1, 2, 3, 4})
