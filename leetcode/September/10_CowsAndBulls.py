from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        countSec = Counter(secret)
        countGues = Counter(guess)
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
                countSec[secret[i]] -= 1
                countGues[guess[i]] -= 1
        for i in range(len(guess)):
            if countSec[guess[i]] > 0 and countGues[guess[i]] > 0:
                countSec[guess[i]] -= 1
                countGues[guess[i]] -= 1
                cows += 1
        return str(bulls) + 'A' + str(cows) + 'B'