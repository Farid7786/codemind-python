n=int(input())
l=list(map(int,input().split()))
k=max(l)
s=[]
if n<3:
    print(k)
else:
    for i in l:
        if i!=k:
            s.append(i)
        else:
            continue
    m=max(s)
    f=[]
    for i in s:
        if i!=m:
            f.append(i)
    print(max(f))