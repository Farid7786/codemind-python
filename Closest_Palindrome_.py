n=int(input())
for i in range(n-1,0,-1):
    sum=0
    h=i
    while h>0:
        r=h%10
        sum=sum*10+r
        h=h//10
    if i==sum:
        copy=i
        break
for j in range(n+1,10000,1):
    add=0
    k=j
    while k>0:
        rem=k%10
        add=add*10+rem
        k=k//10
    if j==add:
        cpy=j
        break
sub=n-copy
mi=cpy-n
if sub>mi:
    print(cpy)
elif sub==mi:
    print(copy,cpy)
else:
    print(copy)