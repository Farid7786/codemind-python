n=int(input())
s=n
sum=0
if n<0:
    n=-n
while n!=0:
    r=n%10
    sum=sum*10+r
    n//=10
if s>0:
    print(sum)
else:
    print(-sum)
        