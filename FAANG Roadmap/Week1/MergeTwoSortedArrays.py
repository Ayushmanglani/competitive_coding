T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(m-1,-1,-1):
        last = a[n-1]
        j = n-2
        while(j>=0 and b[i]<a[j]):
            a[j+1] = a[j]
            j -= 1
        if j != n-2 and b[i]<last:
            a[j+1] = b[i]
            b[i] = last
    for i in a:
        print(i,end=" ")
    for j in b:
        print(j,end=" ")
    print()