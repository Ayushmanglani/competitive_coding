class Solution(object):
    def canReach(self, arr, start):
        n = len(arr)
        visited = [False]*n
        path = [start]

        while path:
            x = path.pop(0)
            visited[x] = True
            if arr[x] == 0:
                return True
            l = x-arr[x]
            h = x+arr[x]
            if l>=0 and visited[l]==False:
                path.append(l)
            if h<n and visited[h]==False:
                path.append(h) 
        return False