n=int(input())
a=list(map(int,input().split()))
k=int(input())
m=a[0]
for i in range(0,len(a)):
    sum=a[i]+k
    if sum>=m:
        m=a[i]
        print("True",end=" ")
    else:
        print("False",end=" ")
    