T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    m = a[-1]
    c = [a[-1]]
    for i in range(n-2,-1,-1):
        if m <= a[i]:
            m = a[i]
            c.append(a[i])
    for i in range(len(c)-1,-1,-1):
        print(c[i],end=" ")
    print()