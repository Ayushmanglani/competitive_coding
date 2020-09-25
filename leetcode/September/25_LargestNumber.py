class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num




class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0: return ""
        
        final_str = ''
        flag = 0
        
		# Arranging the array elements
        for x in range(0, len(nums)-1):
            for y in range(x+1, len(nums)):
                a, b = str(nums[x]), str(nums[y])
                if int(b+a) > int(a+b): 
                    nums[x], nums[y] = nums[y], nums[x]
		# Now the array elements are arranged
        # print(nums)
		
        if nums[0] == 0: return '0'
		
		# iterating through all the newly arranged elements and forming a string version
                   
        while flag < len(nums): 
            final_str += str(nums[flag])
            flag+=1
                    
        return final_str        