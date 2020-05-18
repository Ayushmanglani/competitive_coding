#Sliding Window Approach
import numpy as np
M = 26
def compare(ar1,ar2):
    for j in range(M):
        if ar1[j] != ar2[j]:
            return False
    return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = [0]*M
        countS2 = [0]*M
        ls1 = len(s1)
        ls2 = len(s2)
        if ls2<ls1:
            return False
        for i in range(ls1):
            countS1[ord(s1[i])-97] += 1
            countS2[ord(s2[i])-97] += 1
            
        for i in range(ls1,ls2):
            if compare(countS1,countS2):
                return True
            (countS2[ord(s2[i])-97]) += 1
            (countS2[ord(s2[i-ls1])-97]) -= 1
        
        if compare(countS1,countS2):
            return True
        return False

