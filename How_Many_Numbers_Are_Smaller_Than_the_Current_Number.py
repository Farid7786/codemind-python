n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if i!=j:
            if a[i]>a[j]:
                c=c+1
    print(c,end=" ")