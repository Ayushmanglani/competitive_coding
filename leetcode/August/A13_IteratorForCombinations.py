from itertools import combinations
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        combi = list(combinations(characters, combinationLength))
        self.comb = []
        for i in combi:
            self.comb.append("".join(i))
        self.comb.sort()
        self.len = len(self.comb)
        self.curr = -1
        
    def next(self) -> str:
        self.curr += 1
        return self.comb[self.curr]

    def hasNext(self) -> bool:
        if self.curr+1 < self.len:
            return True
        return False


from itertools import combinations
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.comb = list(map("".join, combinations(characters, combinationLength)))
        
    def next(self) -> str:
        return self.comb.pop(0)

    def hasNext(self) -> bool:
        if self.comb:
            return True
        return False        