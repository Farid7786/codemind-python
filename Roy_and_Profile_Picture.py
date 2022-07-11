t=int(input())
l=int(input())
for i in range(l):
    w,h=map(int,input().split())
    if w<t or h<t:
        print('UPLOAD ANOTHER')
    elif w==h:
        print('ACCEPTED')
    else:
        print('CROP IT')