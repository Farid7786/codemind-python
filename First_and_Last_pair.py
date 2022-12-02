n=int(input())
l=list(map(int,input().split()))
s=[]
d=[]
for i in range(0,len(l)//2):
    s.append(l[i])
for j in range(len(l)//2,len(l)):
   d.append(l[j])
i=0
j=0
d=d[::-1]
while i<len(s) or j<len(d):
    if i<len(s):
        print(s[i],end=' ')
        i+=1
    if j<len(d):
        print(d[j],end=' ')
        j+=1
if n%2!=0:
    print('0')