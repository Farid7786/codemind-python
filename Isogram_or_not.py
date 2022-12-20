n=input()
c=0
k=[]
for i in n:
    if i not in k:
        k.append(i)
    elif i in k:
        c+=1
if c==0:
    print('True')
else:
    print('False')