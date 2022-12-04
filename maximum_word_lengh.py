n=input()
n=n.split(' ')
k=[]
s=[]
c=0
for i in n:
    k.append(len(i))
for i in k:
    if c<i:
        c=i
print(c)