Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#output formatting
a=10
>>> b=12.3
>>> c=codegnan
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c=codegnan
NameError: name 'codegnan' is not defined
>>> c="codegnan"
>>> print(a,b,c)
10 12.3 codegnan
>>> print("a=",a,"b=",b,"c",c)
a= 10 b= 12.3 c codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 12.3 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep=" ")
a= 10 b= 12.3 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep="")
a=10b=12.3c=codegnan
>>> print("a=",a,"b=",b,"c=",c,sep="\n")
a=
10
b=
12.3
c=
codegnan
>>> print("a=",a,"b=",b,"c=",c,sep="\t")
a=	10	b=	12.3	c=	codegnan
>>> 
... print("a=",a,"b=",b,"c=",c,sep="\t",end"\n\n")
SyntaxError: positional argument follows keyword argument
>>> print("a=",a,"b=",b,"c=",c,sep="\t",end="\n\n")
a=	10	b=	12.3	c=	codegnan

>>> print("a=",a,"b=",b,"c=",c,sep="\t",end="@")
a=	10	b=	12.3	c=	codegnan@
>>> print(f"a={a} b={b} c={c}")
a=10 b=12.3 c=codegnan
>>> print("a=%d b=%f c=%s" %(a,b,c))
a=10 b=12.300000 c=codegnan
>>> print("a={} b={} c={}" .format(a,b,c))
a=10 b=12.3 c=codegnan
>>> KeyboardInterrupt
print("a={} b={} c={}" .format(a,b,c))
>>> print("a={0} b={1} c={2}" .format(a,b,c))
a=10 b=12.3 c=codegnan
>>> print("a={2} b={0} c={1}" .format(a,b,c))
a=codegnan b=10 c=12.3
