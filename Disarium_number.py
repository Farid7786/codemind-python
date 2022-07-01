n=int(input())
h=n
sum=0
c=0
add=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
while sum>0:
    r=sum%10
    c+=1
    add=add+(r**c)
    sum=sum//10
if add==h:
    print('True')
else:
    print('False')
    