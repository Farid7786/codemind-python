n=int(input())
p=n
i=0
while n>0:
    i+=1
    n=n//10
n=p*p
k=n%(10**i)
if k==p:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')