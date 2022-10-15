a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=0
c=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if i==j:
            if a[i]>b[j]:
                c=c+1
            elif b[j]>a[i]:
                m=m+1
print(c,m,end=" ")