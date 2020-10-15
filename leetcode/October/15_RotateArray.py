class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        temp = nums.copy()
        l = len(nums)
        for i in range(l):
            nums[(i+k)%l] = temp[i]