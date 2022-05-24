n,m=map(int,input().split())
i=1
gcd=0
while i<=n and i<=m:
    if n%i==0 and m%i==0:
        gcd=i
    i+=1
lcm=(n*m)//gcd
print(lcm)