n=input()
n=n.split()
s=[]
m=[]
c=0
k=0
for i in range(len(n)):
    s.append(min(n[i]))
    m.append(max(n[i]))
while c<len(s) or k<len(m):
        if c<len(s):
            print(s[c],end=' ')
            c+=1
        if k<len(m):
            print(m[k],end=' ')
            k+=1
        