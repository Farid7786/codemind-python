n=int(input())
sum=0
odd=0
a=list(map(int,input().split()))
for i in range(0,len(a)):
    if i%2==0:
        sum=sum+a[i]
    else:
        odd=odd+a[i]
if(sum-odd==0):
    print('YES')
else:
    print('NO')