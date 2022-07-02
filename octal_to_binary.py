n=int(input())
sum=0
i=0
while n>0:
    r=n%10
    sum=sum+(r*(8**i))
    i=i+1
    n=n//10
k=bin(sum).replace("0b","")
print(k)