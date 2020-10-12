class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if A == B and len(set(A)) < len(B): return True
        
        if len(A) != len(B): return False
        
        diff_A = []
        diff_B = []
        
        for i in range(len(A)):
            if A[i] != B[i]:
                diff_A.append(A[i])
                diff_B.append(B[i])
            
        return len(diff_A) == len(diff_B) == 2 and diff_A[::-1] == diff_B

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(set(A)) != len(set(B)):
            return False
        if A == B:
            if len(A) == len(set(A)):
                return False
            else:
                return True
        count = 0
        index = []
        for i in range(len(A)):
            if count > 2:
                return False
            if A[i]!=B[i]:
                count +=1
                index.append(i)
        
        if count == 2:
            i1 = index[0]
            i2 = index[1]
            A = list(A)
            A[i1], A[i2] = A[i2], A[i1]
            A = ''.join(A)
            if A == B:
                return True
            else:
                return False        