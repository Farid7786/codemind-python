n=int(input())
a=list(map(int,input().split()))
k=0
for i in a:
    k=k*10+(i)
k=k+1
s=[]
while k!=0:
    r=k%10
    s.append(r)
    k//=10
s=s[::-1]
print(*s)