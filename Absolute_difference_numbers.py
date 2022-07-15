n,k=map(int,input().split())
c=0
sum=0
add=0
h=n
plus=0
plu=0
cnt=0
ab=bs=0
while n>0:
    r=n%10
    c+=1
    sum=sum*10+r
    n//=10
    if c==k:
        break
while sum>0:
    rem=sum%10
    add=add*10+rem
    sum//=10
while h>0:
    re=h%10
    plus=plus*10+re
    h=h//10
while plus>0:
    rema=plus%10
    cnt+=1
    plu=plu*10+rema
    plus//=10
    if cnt==k:
        break
ab=abs(add-plu)
print(ab)