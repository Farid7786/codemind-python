n=int(input())
m=0
a=list(map(int,input().split()))
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c+=1
    if c==1:
        m+=1
        print(a[i],end=' ')
if m==0:
    print('-1')