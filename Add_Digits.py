n=int(input())
sum=0
while n//10!=0:
    c=0
    while n>0:
        r=n%10
        c=c+r
        n=n//10
    n=c
print(c)