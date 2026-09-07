Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data Types
#int float complex
a=12
type(a)
<class 'int'>
b=13.4
type(b)
<class 'float'>
c=12+4j
type(c)
<class 'complex'>
c=12+6J
c
(12+6j)
# str list tuple
s="Codegnan"
id(s)
2154395414064
s +="Python"
s
'CodegnanPython'
id(s)
2154394725552
s="aaaaaaaa"
s
'aaaaaaaa'
type(s)
<class 'str'>
l =[1,2,3,4,5,5,6]
type(l)
<class 'list'>
id(l)
2154395002432
l.append(12)
l
[1, 2, 3, 4, 5, 5, 6, 12]
id(l)
2154395002432
l=[1,12.3,"str",[1,23]]
type(l)
<class 'list'>
t=(1,2,3,45)
type(t)
<class 'tuple'>
t
(1, 2, 3, 45)
>>> t=(1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> t=(1,12.3,4,"c")
>>> # set dict
>>> s={80,70,24,14,25,78,78,78,78,78}
>>> s
{80, 70, 14, 24, 25, 78}
>>> id(s)
2154395208832
>>> s.add(20)
>>> s
{80, 20, 70, 14, 24, 25, 78}
>>> id(s)
2154395208832
>>> a={1,12.3,"str"}
>>> a
{'str', 1, 12.3}
>>> set(sP)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    set(sP)
NameError: name 'sP' is not defined. Did you mean: 's'?
>>> set(s)
{80, 20, 70, 14, 24, 25, 78}
>>> tppe(s)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    tppe(s)
NameError: name 'tppe' is not defined. Did you mean: 'type'?
>>> type(s)
<class 'set'>
>>> d={"productname":"XYZ","pric":876,"stock":True}
>>> d
{'productname': 'XYZ', 'pric': 876, 'stock': True}
>>> d
{'productname': 'XYZ', 'pric': 876, 'stock': True}
>>> s={1,2,3,4}
>>> s=frozenset({1,1,1,116,18,2,3})
>>> s
frozenset({1, 2, 3, 18, 116})
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
