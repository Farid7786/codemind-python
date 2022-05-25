n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(0,len(a)):
    c=0
    while a[i]>0:
        r=a[i]%10
        c+=1
        a[i]=a[i]//10
    if c%2==0:
        m+=1
print(m)
        
            