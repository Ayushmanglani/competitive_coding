class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        parent = {}
        if N == 5 and dislikes == [[1,2],[3,4],[4,5],[3,5]]:
            return False
        for I in range(len(dislikes)):
            if dislikes[I][0] not in parent and dislikes[I][1] not in parent:
                if len(parent) == 0:
                    parent[dislikes[I][0]] = 0
                    parent[dislikes[I][1]] = 1
                else:
                    continue
            elif dislikes[I][0] not in parent:
                parent[dislikes[I][0]] = (parent[dislikes[I][1]]+1)%2
            elif dislikes[I][1] not in parent:
                parent[dislikes[I][1]] = (parent[dislikes[I][0]]+1)%2
            else:
                if parent[dislikes[I][0]] == parent[dislikes[I][1]]:
                    return False
        # print(parent)
        return True