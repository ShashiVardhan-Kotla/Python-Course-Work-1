Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python operators
#arithmetic operators
a = 10
b = 5
a+b
15
a-b
5
a*b
50
a/b
2.0
a//2
5
a**2
100
2**3
8
16**2
256
12%2
0
#comparision operators
a
10
b
5
a<b
False
a>b
True
a<=b
False
a>=b
True
a>=10
True
a==b
False
a!=b
True
#assignment operators
a=20
a=a+20
a=a+20
a
60
a+=10
a
70
a-=20
a*=20
a
1000
a//=2
a
500
a**=2
a
250000
a/=500
a
500.0
a=100
a%=3
a
1
a
1=
a+=1
a
2
a-=2
a
0
a=10
#relational operators
email=True
password=False
email and password
False
login=True
login=False
display_products=True
login or display_products
True
"s" in "aeiou"
False
"s" not in "aeiou"
True
7%2==0 and 3%2==0
False
6%2==0 and 3%2==0
False
6%2==0 or 3%2==0
True
3%2==0
False
not 3%2==0
True
#membership operators
s="python programming"
"python" in s
True
"java" in s
False
"z" in s
False
"a" in s
True
"c++" not in s
True
"program" not in s
False
l=[1,2,3,4]
3 in l
True
9 not in l
True
1 not in l
False
t=(20,30,40,50,)
50 in t
True
30 not in t
False
s={"pen", "paper", "book"}
"book" not in s
False
"bag" not in s
True
"pen" in s
True
data={"name":"dinesh","batch":65,"course":"pfs"}
"dinesh" in data
False
65 in data
False
"batch" in data
True
"age" in data
False
"dob" in data
False
>>> #identity operators
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> id(l)
1543898996544
>>> id(m)
1543906708992
>>> l==m
True
>>> l is m
False
>>> n=m
>>> n
[1, 2, 3, 4]
>>> id(n)
1543906708992
>>> m is n
True
>>> n is m
True
>>> n is l
False
>>> n is not l
True
>>> #bitwise operators
>>> 11 & 12
8
>>> 11 | 15
15
>>> 11 ^ 12
7
>>> 2<<2
8
>>> 2<<3
16
>>> 2<<4
32
>>> 16>>2
4
>>> ~14
-15
>>> ~78
-79
>>> ~23
-24
