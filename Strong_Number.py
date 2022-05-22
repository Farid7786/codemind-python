n=int(input())
sum=0
h=n
while n>0:
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if sum==h:
    print('The number',h,'is a strong number')
else:
    print('The number',h,'is not a strong number')
        