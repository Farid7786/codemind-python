n=input()
n=n.lower()
n=n.split( )
s='aeiou'
k=[]
m=[]
for i in n:
    for j in i:
        if j in s:
            k.append(j)
for i in s:
    if i not in k:
        m.append(i)
if m==[]:
    print(0)
else:
    l=sorted(m)
    print(*l)

            