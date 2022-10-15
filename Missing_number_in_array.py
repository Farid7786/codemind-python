t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n+1,1):
        if i not in a:
            print(i)
            break
    t=t-1    