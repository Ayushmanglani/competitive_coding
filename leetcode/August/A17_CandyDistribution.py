class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        r = [0]*num_people
        i = 0
        k = 1
        while candies>0:
            if i == num_people:
                i = 0
            if k < candies:                 
                r[i] += k
                candies -= k
            else:
                r[i] += candies
                candies = 0
            k+=1
            i+=1
        return r