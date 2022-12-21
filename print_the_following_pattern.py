ch=int(input())
l=65+ch
k=[]
for i in range(65,l):
    k.append(chr(i))
k=k[::-1]
for i in k:
    for j in range(0,ch):
        print(i,end=' ')
    ch=ch-1
    print()