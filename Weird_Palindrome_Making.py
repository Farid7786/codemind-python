t=int(input())
while t!=0:
    n=int(input())
    c=m=0
    a=list(map(int,input().split()))
    for i in range(0,len(a)):
        if a[i]%2!=0:
            c+=1
        else:
            m+=1
    k=c//2
    print(k,end='
')