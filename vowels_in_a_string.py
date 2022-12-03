n=input()
s=input()
c=0
d=0
for i in n:
    if s in i:
        print('True')
        print(c)
        d+=1
        break
    c+=1
if d==0:
    print('False')