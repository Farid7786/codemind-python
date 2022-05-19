n=int(input())
sum=0
prod=1
while n:
    r=n%10
    sum=sum+r
    prod=prod*r
    n=n//10
sub=prod-sum
print(sub)