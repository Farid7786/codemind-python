t=int(input())
for i in range(t):
    n=input()
    for j in n:
        if j.isdigit():
            print('Yes')
            break
    else:
        print('No')