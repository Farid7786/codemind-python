n=int(input())
a=list(map(int,input().split()))
copy=0
k=1000
t=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c+=1
    if c==a[i]:
        if a[i]<k:
            k=a[i]
        elif a[i]>copy:
            copy=a[i]
        t+=1
if t==0:
    print('-1')
else:
    print(k,copy)