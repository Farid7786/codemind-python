n=int(input())
sum=0
prod=1
while n>0:
    r=n%10
    sum=sum+r
    prod=prod*r
    n=n//10
if sum==prod:
    print('Spy Number')
else:
    print('Not Spy Number')