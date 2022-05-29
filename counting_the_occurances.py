a=input()
b=input()
c=0
d=10000000
for i in a:
    if b in i:
        c+=1
if c!=0:
    print(c)
else:
    print('-1')