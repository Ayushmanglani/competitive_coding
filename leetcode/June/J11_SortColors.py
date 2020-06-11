class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = [0,0,0]
        for i in nums:
            c[i] += 1
        k = 0
        for i in range(3):
            for _ in range(c[i]):
                nums[k] = i
                k += 1
        