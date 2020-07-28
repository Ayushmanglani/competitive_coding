class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_map = [0]*26
        for i in tasks:
            char_map[ord(i)-65] += 1
        
        char_map.sort()
        max_value = char_map[25]
        freq = (max_value-1)*n
        for i in range(24,-1,-1):
            freq -=  min(max_value-1, char_map[i])
        
        if freq<0:
            return len(tasks)
        return(len(tasks)+freq)

class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        counts = collections.Counter(tasks)
        counts = list(counts.values())
        res = (n+1)*(max(counts)-1)+counts.count(max(counts))
        return max(res,len(tasks))