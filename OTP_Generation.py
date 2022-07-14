n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
while sum>0:
    rem=sum%10
    sum=sum//10
    if rem%2==0:
        continue
    else:
        b=rem*rem
        print(b,end='')