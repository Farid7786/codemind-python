n=int(input())
m=int(input())
sum=0
add=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
for i in range(1,m):
    if m%i==0:
        add=add+i
if sum==m and add==n:
    print('Amicable')
else:
    print('Not Amicable')