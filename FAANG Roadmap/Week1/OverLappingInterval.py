T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    A = []
    for i in range(0,n*2,2):
        A.append([a[i],a[i+1]])
    A = sorted(A, key = lambda i: i[0])
    for i in range(n-1):
        if A[i][1] >= A[i+1][0]:
            A[i][1] = max(A[i][1],A[i+1][1])
            A[i+1] = A[i]
            A[i] = None
    for i in range(n):
        if A[i] != None:
            print(A[i][0],end=" ")
            print(A[i][1],end=" ")
    print()