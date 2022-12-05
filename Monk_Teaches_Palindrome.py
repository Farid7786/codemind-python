t=int(input())
for i in range(t):
    n=input()
    n=n.split()
    for j in n:
        if j==j[::-1]:
            if len(j)%2==0:
                print('YES EVEN')
                break
            else:
                print('YES ODD')
                break
        else:
            print('NO')