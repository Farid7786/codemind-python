t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n>0 and m>0:
        for i in range(1,m+1):
            if (i*i)%m==n:
                print(i)
                break
        else:
            print('-1')
    else:
        print('0')