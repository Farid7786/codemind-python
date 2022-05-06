n=int(input())
sum=0
k=n
while k>0:
    r=k%10
    sum=sum+r
    k=k//10
if n%sum==0:
    print('True')
else:
    print('False')