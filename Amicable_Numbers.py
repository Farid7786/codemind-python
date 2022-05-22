n=int(input())
m=int(input())
p=m
k=n
sum=0
add=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
for j in range(1,m):
    if m%j==0:
        add=add+j
if sum==p and add==k:
    print('Amicable')
else:
    print('Not Amicable')