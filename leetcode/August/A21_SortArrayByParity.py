class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        
        while i < j:
            if A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                i -= 1
                j -= 1
            i += 1
        return A

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        O = []
        E = []
        for i in A:
            if i%2 != 0:
                O.append(i)
            else:
                E.append(i)
        return E+O

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key = lambda x: x%2)
        return A