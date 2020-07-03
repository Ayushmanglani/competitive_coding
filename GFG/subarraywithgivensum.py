import numpy as np
T = int(input())
for _ in range(T):
    n,s = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*(n+1)
    st = 1
    found = 0
    for i in range(n):
        b[i+1] = a[i]+b[i]
        if b[i+1] == s:
            print(st,i+1)
            found = 1
            break
        elif b[i+1] > s:
            while b[i+1] > s:
                p = a[st-1]
                b[i+1] -= p
                st += 1
            if b[i+1] == s:
                print(st,i+1)
                found = 1
                break
    if found == 0:
        print(-1)