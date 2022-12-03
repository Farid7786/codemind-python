n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
k=[]
for i in a:
    if i in b:
        s.append(i)
for j in b:
    if j in a:
        s.append(j)
for i in s:
    if i not in k:
        k.append(i)
print(*k)