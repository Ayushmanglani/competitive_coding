class StreamChecker:
    def __init__(self, words: List[str]):
        # build the trie of reverse words
        T = lambda: defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
        self.s = ''
        self.L = max(map(len, words))

    def query(self, letter: str) -> bool:
        # query directly
        self.s = (letter + self.s)[:self.L]
        node = self.trie
        for x in self.s:
            if x in node:
                node = node[x]
                if '#' in node:
                    return True
            else:
                break
        return False