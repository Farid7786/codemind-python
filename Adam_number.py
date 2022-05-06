n=int(input())
rt=n*n
sum=0
secsum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
sqt=sum*sum
while sqt>0:
    t=sqt%10
    secsum=secsum*10+t
    sqt=sqt//10
if rt==secsum:
    print('True')
else:
    print('False')
    
    
    