n=int(input())
if n==1 or n==0:
    print('True')
else:
    a=0
    b=1
    c=a+b
    while n>c:
        a=b
        b=c
        c=a+b
    if n==c:
        print('True')
    else:
        print('False')
            
    