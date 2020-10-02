class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def helper(cur, target, cur_sum, index):
            if target == cur_sum:
                res.append(cur)
            find = target - cur_sum
            for i in range(index, len(candidates)):
                a = candidates[i]
                if a > find:
                    break
                helper(cur+[a], target, cur_sum+a, i)
        
        helper([], target, 0, 0)
        return res

class Solution:
    def recursor(self, target, order, index):
        for i, x in enumerate(self.candidates[index :]):
            if target >= 2 * x:
                self.recursor(target - x, order + [x], index + i)
            elif x == target:
                self.ans.append(order + [x])
            elif x > target:
                break

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.candidates = sorted(candidates)
        self.recursor(target, [], 0)
        return self.ans        