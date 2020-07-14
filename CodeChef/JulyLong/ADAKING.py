T = int(input())
for _ in range(T):
    k = int(input())
    A = [[-1 for _ in range(8)] for i in range(8)]
    count = 0
    for i in range(8):
        for j in range(8):
            A[i][j]=1
            count += 1
            if(count==k): break
        if(count == k): break
    print('O',end="")
    for i in range(8):
        for j in range(8):
            if not(i==0 and j==0):
                if(A[i][j]==(-1)):
                    print('X',end="")
                else:
                    print('.',end="")
        print()
    print()