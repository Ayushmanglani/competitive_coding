class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        swaps = []
        for n in range(len(A),1,-1):
            m = max(A[:n])
            if m == A[n-1]:
                continue
            if A[0] != m:
                i = A.index(m,0,n)
                swaps.append(i+1)
                A[:i+1] = A[i::-1]
            swaps.append(n)
            A[:n] = A[n-1::-1]
        return swaps

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(A): 
            return A[::-1]
                    
        end=len(A)
        res=[]
        while end>1:
            maxInd=A.index(max(A[:end])) #step 1 get max
            if maxInd==end-1: #if Max already at the end then its in the right place decrement end and continue
                end-=1
                continue

            #making the max element at Index 0, unless if it already was at index 0
            if maxInd!=0:
                A=flip(A[:maxInd+1])+A[maxInd+1:] 
                res.append(maxInd+1) #append flipping size which is maxInd+1
                
                
            #Now max is at ind=0, flip whole array to make it at the "end"
            A=flip(A[:end])+A[end:]
            res.append(end)
            
            end-=1 #decrement end
        return res 

                