n=int(input())
rt=n*n
sum=0
while rt>0:
    r=rt%10
    sum=sum+r
    rt=rt//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')
    