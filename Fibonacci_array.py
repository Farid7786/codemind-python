n=int(input())
l=list(map(int,input().split()))
s=[]
a=l[0]
b=l[1]
s.append(a)
s.append(b)
c=a+b
k=0
if n>3:
    while k<n-2:
        s.append(c)
        a=b
        b=c
        c=a+b
        k+=1
    cnt=0
    for i in s:
        if i in l:
            cnt+=1
    if cnt==n:
        print('yes')
    else:
        print('no')
else:
    print('no')