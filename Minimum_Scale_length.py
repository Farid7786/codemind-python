n=int(input())
a=list(map(int,input().split()))
max=a[0]
j=1
while j<n:
    if a[j]%max==0:
        j+=1
    else:
        max=a[j]%max
print(max);