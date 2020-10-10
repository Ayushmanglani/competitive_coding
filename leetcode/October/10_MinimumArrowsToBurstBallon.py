class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Base Case: zero balloons
        """
        if points == []:
            return 0
        """
        Initialize/Setup:
        - Sort balloons by minimum x coordinate
        - Initialize maximum end of a balloon (max_end) to end
          of the first balloon.
        - number of arrows (num_arrows) set to 0
        """
        points.sort()
        max_end = points[0][1]
        num_arrows = 0        
        """
        Burst Balloons
        - If a balloon end (xmax) is less than the current maximum
          (max_end), adjust the current maximum.
        - If a balloon start is beyond the current maximum end
          of a balloon, expend an arrow to burst preceding balloons
          and set max_end to end of the new balloon.
        """
        for xmin, xmax in points:
            if xmax < max_end:
                max_end = xmax
            elif xmin > max_end:
                num_arrows += 1
                max_end = xmax
        return num_arrows + 1

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0        
        points.sort(key=lambda x: (x[1], x[0]))
        end = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if points[i][0] <= end:
                end = min(end, points[i][1])
            else:
                count += 1
                end = points[i][1]                
        return count        

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points = sorted(points, key=lambda x: x[1])
        num = 1
        end = points[0][1]
        for point in points:
            if point[0] > end:
                num += 1
                end = point[1]                
        return num        