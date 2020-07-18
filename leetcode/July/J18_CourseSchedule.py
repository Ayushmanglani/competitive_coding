from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        
        stack = []
        visited = [False]*numCourses
        recStack = [False]*numCourses
        
        def depth(v,stack):
            visited[v] = True
            recStack[v] = True           
            for i in graph[v]:
                if visited[i] == False:
                    if depth(i,stack):
                        return True
                elif recStack[i] == True: 
                    return True
            stack.insert(0,v)  
            recStack[v] = False
            return False
                   
        def traverse(numCourses):            
            for i in range(numCourses):
                if visited[i] == False:
                    if depth(i,stack):
                        return True
            return False   
        
        if not traverse(numCourses):
            return(stack[::-1])


#method 2
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        status = [0]*numCourses
        graph = collections.defaultdict(list)
        for c, pre in prerequisites:
            graph[pre].append(c)
        stack = []
        def dfs(course):
            if status[course] == 1:
                return False  # circle case
            if status[course] == 2:  # visited
                return True
            status[course] = 1  # visiting
            for c in graph[course]:
                if not dfs(c):
                    return False
            stack.append(course)
            status[course]  = 2
            return True
        for course in range(numCourses):
            if status[course] == 0:
                if not dfs(course):
                    return []
        return stack[::-1]