import math
class Solution:
    def countBits(self, num: int) -> List[int]:
        A = [0]
        B = [2,4,8,16,32,64,128,256,512,1024,2048,4096]
        for i in range(1,num+1):
            if i in B:
                x = 1
            elif i%2 == 0:
                x = A[i//2]
            else:
                x = A[i//2] + 1
            A.append(x)
        return(A)