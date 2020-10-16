class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        for i in range(m):
            if target > matrix[i][-1]:
                continue
            else:
                l = 0
                h = n-1
                while l<=h:
                    mid = (l+h)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        h = mid-1
                    else:
                        l = mid+1
                return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        M, N = len(matrix), len(matrix[0])
        
        l, r = 0, M*N - 1
        
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // N][mid % N]
            
            if target == val:
                return True
            elif target < val:
                r = mid - 1
            else:
                l = mid + 1
        
        return False                