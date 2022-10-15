n=int(input())
a=list(map(int,input().split()))
k=n//2
sum=0
p=0
for i in range(0,k):
    sum=sum+a[i]
for j in range(k,len(a)):
    p=p+a[j]
if p>sum:
    s=p-sum
else:
    s=sum-p
if s%4==0:
    print("X")
else:
    print("Y")