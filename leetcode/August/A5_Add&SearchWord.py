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