T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        print(1)
    else:
        found = 0
        s = a[0]
        st = sum(a)-(a[0])
        for i in range(1,n-1):
            st -= a[i]
            if s == st:
                print(i+1)
                found = 1
                break
            s += a[i]
        if found == 0:
            print(-1)