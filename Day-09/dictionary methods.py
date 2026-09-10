Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #mut ord het dyn unidu
>>> d = {}
>>> type(d)
<class 'dict'>
>>> d = {1:4,2:8,3:13}
>>> d
{1: 4, 2: 8, 3: 13}
>>> d = {}
>>> d[1]=1
>>> d[12.3]=1
>>> d['str']=1
>>> d[(1,2,4)]=1
>>> d[(2+3j)]=1
>>> d[True]=1
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1}
>>> d[False]=1
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]='str'
>>> d[4]=2+3j
>>> d[5]=True
>>> d[6]=[1,2,3]
>>> d[7]=(1,2,3)
>>> d[8]={1,2,3}
>>> d[9]=frozenset({1,2,3})
>>> d[10]={1:1,2:2}
>>> d[11]=None
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}
>>> d={}
>>> d[1]=2
>>> d
{1: 2}
>>> d[1]=3
>>> d
{1: 3}
>>> data = {'name':'vardhan','course':'pfs','batch':65}
>>> data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65}
>>> 'vardhan' in data
False
65 in data
False
'course' in data
True
data['name']
'vardhan'
data['batch']
65
data.get('name')
'vardhan'
data.get('batch')
65
data.get('age')
data.get('age' 'key is not present')
data.get('age','key is not present')
'key is not present'
data.get('batch','key is not present')
65
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65}
data['age']=21
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65, 'age': 21}
data['phno']=9876543210
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9876543210}
data.update({'email': 'kotlavardhan5@gmail.com','py':2027})
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9876543210, 'email': 'kotlavardhan5@gmail.com', 'py': 2027}
data.popitem()
('py', 2027)
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9876543210, 'email': 'kotlavardhan5@gmail.com'}
data.pop('age')
21
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65, 'phno': 9876543210, 'email': 'kotlavardhan5@gmail.com'}
del data['phno']
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65, 'email': 'kotlavardhan5@gmail.com'}
del data['batch']
data
{'name': 'vardhan', 'course': 'pfs', 'email': 'kotlavardhan5@gmail.com'}
data.pop('email')
'kotlavardhan5@gmail.com'
data
{'name': 'vardhan', 'course': 'pfs'}
data.clear()
d
{1: 3}
data
{}
data.values()
dict_values([])
len(data)
0
data.keys()
dict_keys([])
data.values()
dict_values([])
data.items()
dict_items([])
sorted(data)
[]
max(data)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    max(data)
ValueError: max() iterable argument is empty
max(a)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    max(a)
NameError: name 'a' is not defined
data={'name':'vardhan','course':'pfs','batch':65}
max(data)
'name'
min(data)
'batch'
d = {1:1,2:2}
m = d
d
{1: 1, 2: 2}
m[3]=3
d
{1: 1, 2: 2, 3: 3}
n=d.copy()
n[4]=4
n
{1: 1, 2: 2, 3: 3, 4: 4}
d
{1: 1, 2: 2, 3: 3}
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65}
data.get('py')
data.setdefault('py',2026)
2026
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65, 'py': 2026}
data.setdefault('name',2026)
'vardhan'
data.setdefault('email',2026)
2026
data.setdefault('key',2026)
2026
data
{'name': 'vardhan', 'course': 'pfs', 'batch': 65, 'py': 2026, 'email': 2026, 'key': 2026}
dict
<class 'dict'>
