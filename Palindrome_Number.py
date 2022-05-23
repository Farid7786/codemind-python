t=int(input())
while t>0:
    sum=0
    n=int(input())
    h=n
    while n>0:
        r=n%10
        sum=sum*10+r
        n=n//10
    if sum==h:
        print('True')
    else:
        print('False')
t-=1