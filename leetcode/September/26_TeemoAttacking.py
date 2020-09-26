class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total = duration
        last = timeSeries[0]+duration-1
        
        for i in range(1,len(timeSeries)):
            if timeSeries[i]<last and timeSeries[i]+duration>last:
                total += duration+timeSeries[i]-last-1
            elif timeSeries[i]>last:
                total += duration                
            elif timeSeries[i]==last:
                total += duration-1
            last = timeSeries[i]+duration-1
        return total

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries: return 0
        total = 0
        
        for i in range(1, len(timeSeries)):
            total += min(timeSeries[i]-timeSeries[i-1], duration)
            
        return total+duration        