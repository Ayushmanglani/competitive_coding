class Solution(object):
    def validMountainArray(self, arr):
        n = len(arr)
        if n<2:
            return False
        inc = 0
        dec = 0
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] < arr[i+1]:
                if dec != 0:
                    return False
                inc = 1
            else:
                if inc != 1:
                    return False
                dec = 1
        if dec == 1 and inc == 1:
            return True
        return False

class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0
        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1
        return i == N-1        