class Solution(object):
    def canPlaceFlowers(self, f, n):
        L, i, c, f = len(f)-2, -2, 0, f + [0]
        while i < L:
        	i += 2
        	if f[i] == 1: continue
        	if f[i+1] == 0: c += 1
        	else: i += 1
        return n <= c

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                count = count + 1
        
        return n <= count        