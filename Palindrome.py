n=int(input())
sum=0
h=n
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if h==sum:
    print('True')
else:
    print('False')