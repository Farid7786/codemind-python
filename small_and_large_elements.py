n=input()
n=n.split()
k=[]
for i in n:
    k.append(min(i))
    break
n=n[::-1]
for i in n:
    k.append(max(i))
    break
print(*k)