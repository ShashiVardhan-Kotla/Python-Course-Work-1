'''
n = int(input("Enter the input: "))
res = []
for i in range(1,n+1):
    if n%i==0:
        res.append(i)

print(f'Factors of {n} = {res}') 

s = 'python programming'
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
s = 'aaaaaaasssssssdddddbbccccttaaa'
compressed=''
count=1
res =''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        res+= s[i]+str(count)
        count=1
print(res+s[i]+str(count))            

