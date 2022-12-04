n=input()
n=n.split()
s='AEIOUaeiou'
max=0
for i in n:
    c=0
    for j in i:
        if j in s:
            c+=1
    if max<c:
        max=c
print(max)