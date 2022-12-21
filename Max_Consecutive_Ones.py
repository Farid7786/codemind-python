n=int(input())
a=list(map(int,input().split()))
c=0
k=[]
for i in range(0,len(a)):
    if a[i]==0:
        c=0
    else:
        c+=1
    k.append(c)
print(max(k))