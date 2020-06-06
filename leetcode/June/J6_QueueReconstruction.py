class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda i: (-i[0],i[1]))
        a = []
        for i in people:
            a.insert(i[1],i)
        return(a)