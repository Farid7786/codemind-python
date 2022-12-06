n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,len(l)):
    s=(l[i]**2)
    k.append(s)
print(*sorted(k))