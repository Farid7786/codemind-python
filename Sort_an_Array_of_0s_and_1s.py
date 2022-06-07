n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    if a[i]==0:
        print(a[i],end=' ')
for j in range(0,len(a)):
    if a[j]==1:
        print(a[j],end=' ')