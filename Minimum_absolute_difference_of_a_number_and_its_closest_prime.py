n=int(input())
cpy=0
m=0

count=0
for l in range(1,n+1):
    if n%l==0:
        count+=1
if count==2:
    print("0")
else:
    for i in range(n,1,-1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            m=i
            break
    for k in range(n+1,100000):
        cnt=0
        for t in range(1,k+1):
            if k%t==0:
                cnt+=1
        if cnt==2:
            cpy=k
            break
    ab=abs(m-n)
    bs=abs(cpy-n)
    if ab>bs:
        print(bs)
    else:
        print(ab)