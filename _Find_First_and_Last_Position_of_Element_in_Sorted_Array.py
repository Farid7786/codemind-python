n=int(input())
a=list(map(int,input().split()))
se=int(input())
c=m=0
for i in range(0,n):
    if se==a[i]:
        print(i,end=' ')
        c+=1
        break
for j in range(len(a)-1,-1,-1):
    if se==a[j]:
        print(j)
        m+=1
        break
if c==0 and m==0:
    print('-1 -1')