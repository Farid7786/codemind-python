n=int(input())
c=sum=m=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
while n:
    r=n%10
    sum=sum*10+r
    n=n//10
for j in range(1,sum+1):
    if sum%j==0:
        m+=1
if c==2 and m==2:
    print('circular prime')
elif c==2 and m!=2:
    print('prime but not a circular prime')
elif c!=2 and m!=2:
    print('not prime')