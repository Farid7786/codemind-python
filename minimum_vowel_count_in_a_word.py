n=input()
s='AEIOUaeiou'
n=n.split()
min=1000
for i in n:
    c=0
    for j in i:
        if j in s:
            c+=1
    if min>c:
        min=c
print(min)