n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    prod=1
    for j in range(0,len(a)):
        if(a[i]!=a[j]):
            prod=prod*a[j]
    print(prod,end=' ')