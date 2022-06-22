n=int(input())
a=list(map(int,input().split()))
ma=cnt=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c+=1
    if c==1 and ma<a[i]:
        ma=a[i]
        cnt+=1
if cnt==0:
    print('-1')
else:
    print(ma)
        