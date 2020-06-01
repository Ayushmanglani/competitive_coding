class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[-1][0]
        y2 = coordinates[-1][1]
        try:
            if x2 == x1:
                for i in range(1,len(coordinates)-1):
                    if coordinates[i][0] != x1:
                        return False
            m = ((x2-x1)/(y2-y1))
            for i in range(1,len(coordinates)-1):
                p = ((m)*(coordinates[i][1]-y1)) - (coordinates[i][0] - x1)
                if p != 0.0:
                    return False
                    break
            return True    
        except:
            return 
