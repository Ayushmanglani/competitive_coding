from collections import defaultdict


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self._dict[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        len_word = len(word)
        for candidate in self._dict[len_word]:
            match = True
            for i in range(len_word):
                if not (word[i] in (candidate[i], ".")):
                    match = False
                    break
            if match:
                return True
        return False

#Method 2
class WordDictionary:

    def __init__(self):
        
        self.node = {}

    def addWord(self, word: str) -> None:
        
        
        n = self.node
        for letter in word:
            if letter not in n:
                n[letter] = {}
            n = n[letter]
        n['end'] = 'yes' # indicates end of a word

    def search(self, word: str) -> bool:
        
        def sUtil(word,node):
            if len(word) == 0:
                return "end" in node # if the word in the tree ends here. Then return True else False.
            
            if word[0] == '.': 
                ans = False
                for k in node:
                    if k!='end':
                        ans = ans or sUtil(word[1:],node[k]) 
                return ans
            elif word[0] in node:
                node = node[word[0]]
                return sUtil(word[1:],node)
            else:
                return False
        
        return sUtil(word,self.node)