def duplicates(arr, n): 
    res = []
    a = [0]*n
    for i in arr: 
        a[i] += 1
    for i in range(n):
        if a[i] > 1:
            res.append(i)
    if nor res:
        res.append(-1)    
    return res