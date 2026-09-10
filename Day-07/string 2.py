Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Triming methods
s = '     Hello world    '
s.strip()
'Hello world'
s.rstrip()
'     Hello world'
s.replace(' ','')
'Helloworld'
s = 'java', 'python', 'flask-mysql-fastapi=c'
s
('java', 'python', 'flask-mysql-fastapi=c')
s = 'java-python-flask-mysql-fastapi=c'
s
'java-python-flask-mysql-fastapi=c'
s.split('-',2)
['java', 'python', 'flask-mysql-fastapi=c']
s.rsplit('-',2)
['java-python-flask', 'mysql', 'fastapi=c']
l = '''python'''
l = '''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c =['python', 'java', 'mysql', 'flask']
c
['python', 'java', 'mysql', 'flask']
''.join(c)
'pythonjavamysqlflask'
', '.join(c)
'python, java, mysql, flask'
'@'.join(c)
'python@java@mysql@flask'
>>> '-'.join({'1', '2', '3'})
'2-3-1'
>>> a = 'strings.py'
>>> a.partition('.')
('strings', '.', 'py')
>>> a = 'string.py.java.png.txt'
>>> s
'java-python-flask-mysql-fastapi=c'
>>> a
'string.py.java.png.txt'
>>> a.partition('.')
('string', '.', 'py.java.png.txt')
>>> a.rpartition('.')
('string.py.java.png', '.', 'txt')
>>> a = 'strings.png'
>>> a.startswith('list')
False
>>> a.endswith('.png')
True
>>> 'pythnv.13'.islower()
True
>>> 'Python.13'.islower()
False
>>> 'PYTHON234567@#%$^&'.isupper()
True
>>> 'estyu'.isalpha()
True
>>> 'estyu8765@'.isalpha()
False
>>> 'serdtfyguhjkl'.isalnum()
True
>>> '987654'.isalnum()
True
>>> '      '.isspace()
True
>>> 'Hlo Wor'.istitle()
True
>>> 'HLO Word'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> a.partition('.')
('strings', '.', 'png')
