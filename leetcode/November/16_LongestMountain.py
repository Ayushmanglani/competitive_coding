class Solution(object):
    def longestMountain(self, A):
        large = 0
        inc = 0
        dec = 0
        n = len(A) 
        for i in range(len(A)-1):            
            if A[i+1]>A[i]:
                if dec > 0:
                    large = max(large,inc+dec+1)
                    dec = 0
                    inc = 0
                inc += 1                 
            elif A[i+1]==A[i]:
                if inc>0 and dec>0:
                    large = max(large,inc+dec+1)
                inc = 0
                dec = 0
            else:
                if inc>0:
                    dec += 1           
        if inc>0 and dec>0:
            large = max(large,inc+dec+1)
        return large