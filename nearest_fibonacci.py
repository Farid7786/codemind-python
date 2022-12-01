n=int(input())
a=0
b=1
c=a+b
while c<=n:
    a=b
    b=c
    c=a+b
sum=n-b
sub=c-n
if sum>sub:
    print(c)
elif sum==sub:
    print(b,c)
else:
    print(b)