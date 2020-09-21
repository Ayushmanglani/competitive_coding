class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]
            
        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False
        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        steps = []
        for trip in trips:
            steps.append([trip[1], trip[0]])
            steps.append([trip[2], -trip[0]])
        steps.sort()
        for step in steps:
            capacity -= step[1]
            if capacity < 0:
                return False
        return True        