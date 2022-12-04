n=input()
n=n.split(' ')
for i in range(0,len(n)):
    if i%2==0:
        c=n[i]
        print(c[::-1],end=' ')
    else:
        print(n[i],end=' ')
        
        