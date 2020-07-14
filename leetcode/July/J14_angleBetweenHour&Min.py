class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hrminutes = ((hour%12)+(minutes/60))*5
        angle = abs(hrminutes-minutes)*6
        return(min(360-angle,angle))