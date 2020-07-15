T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mis = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            print(a[i],end=" ")
            break
    for i in range(n-1):
        if a[i]+2 == a[i+1]:
            print(a[i]+1)
            mis = 1
            break
    if mis == 0:
        if a[0] == 1:
            print(n)
        else:
            print(1)

#method2
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    new = [0]*(n)
    rep = -1
    for i in a:
        new[i-1] += 1
        if new[i-1] > 1:
            rep = i
    mis = new.index(0)+1
    print(rep,mis)