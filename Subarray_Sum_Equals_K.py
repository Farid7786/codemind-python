n,k=map(int,input().split())
arr=list(map(int,input().split()))
sum=0
c=0
for i in range(0,len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum=sum+arr[j]
        if sum==k:
            c+=1
print(c)