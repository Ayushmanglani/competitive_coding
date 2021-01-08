class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        str1 = ''.join(map(str, word1))
        str2 = ''.join(map(str, word2))
        return (str1==str2)

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):        
        return ''.join(word1) == ''.join(word2)        