n=input()
n=n[::-1]
n=n.split()
for i in n:
    s=min(i)
    break
m=s.lower()
for i in n:
    if m in i:
        print(m)
        break
    else:
        print(s)