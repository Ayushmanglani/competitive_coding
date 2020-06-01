class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(A) and j < len(B):
            a_left, a_right = A[i]
            b_left, b_right = B[j]

            if a_right < b_right:
                i += 1
            else:
                j += 1

            if a_right >= b_left and b_right >= a_left:
                ends = sorted([a_left, a_right, b_left, b_right])
                res.append([ends[1], ends[2]])

        for r in range(len(res)-1):
            if res[r][1] == res[r+1][0]:
                res[r:r+2] = [[res[r][0], res[r+1][1]]]

        return res