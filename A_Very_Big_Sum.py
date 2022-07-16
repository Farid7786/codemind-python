n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,len(a)):
    sum+=a[i]
print(sum)