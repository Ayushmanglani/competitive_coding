T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    mid = 0
    low = 0
    high = n-1
    while mid <= high:
        if a[mid] == 0:
            a[mid],a[low] = a[low],a[mid]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid],a[high] = a[high],a[mid]
            high -= 1
    for i in range(n):
        print(a[i],end=" ")
    print()