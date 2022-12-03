n=input()
s='AEIOUaeiou'
k=[]
for i in n:
    if i in s:
        if i not in k:
            k.append(i)
for m in k:
    print(m,end=' ')