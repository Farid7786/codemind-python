n=int(input())
c=0
for i in range(1,n):
    sum=(i*(i+1))
    if n==sum:
        c+=1
if c==1:
    print('YES')
else:
    print('NO')