class Solution(object):
    def findKthPositive(self, arr, k):
        n = len(arr)
        j = 0
        f = 0
        for i in range(1,n+k+1):
            if j<n and i == arr[j]:
                j += 1
                continue
            else:
                f += 1
                if k == f:
                    return i