n=int(input())
m=int(input())
for i in range(n,m+1):
    k=i
    sum=0
    while i>0:
        r=i%10
        sum=sum*10+r
        i=i//10
    if sum==k:
        print(sum,end=' ')