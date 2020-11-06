class Solution(object):
    def minCostToMoveChips(self, position):
        odd_numbers = 0
        even_numbers = 0
        for num in position:
            if num % 2 ==0:
                even_numbers += 1
            else:
                odd_numbers += 1
        return min(odd_numbers, even_numbers)