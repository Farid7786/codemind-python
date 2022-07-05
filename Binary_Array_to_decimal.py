n=int(input())
a=list(map(int,input().split()))
sum=0
j=n-1
for i in range(len(a)):
    if j>=0:
        sum=sum+(a[i]*(2**j))
        j-=1
print(sum)