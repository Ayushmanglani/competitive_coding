class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = 50
        while idx > 40:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
        return 1 + (idx - 1) % 10

class Solution:
    def rand10(self):
        a = [1,2,3,4,5,6,7,8,9,10]
        return random.choice(a)        