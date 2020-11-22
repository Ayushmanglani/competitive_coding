class Solution(object):
    def uniqueMorseRepresentations(self, words):
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        x = {}
        output = 0
        for word in words:
            s = ""
            for l in word:
                s += d[ord(l)-97]            
            if s not in x:
                x[s] = True
                output += 1
        return output