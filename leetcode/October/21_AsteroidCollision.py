class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []
        
        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                
                if abs(new) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(new):
                    stack.pop()
                break
                
            else:
                stack.append(new)
                
        return stack