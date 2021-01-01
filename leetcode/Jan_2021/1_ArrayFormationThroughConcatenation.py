class Solution(object):
    def canFormArray(self, arr, pieces):
        pieces = sorted(pieces, key=len, reverse=True) 
        for i in range(len(pieces)):
            j = 0
            k = len(pieces[i])
            while j<len(arr):
                if pieces[i] == arr[j:j+k]:
                    arr = arr[:j] + arr[j+k:]
                j += 1
        if arr:
            return False
        return True
