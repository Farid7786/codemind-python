n=int(input())
a=[]
while n>0:
    r=n%10
    a.append(r)
    n//=10
for i in range(len(a)-1,-1,-1):
    if a[i]==6:
        a[i]=9
        break
for j in range(len(a)-1,-1,-1):
    print(a[j],end='')
    