class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,1
        add = 'y'
        Finalx = 0
        Finaly = 0
        for action in instructions:
            if action == 'L':                
                if x == 0:
                    x = -1*(y)
                    y = 0
                else:
                    y = x
                    x = 0
            elif action == 'R':
                if x == 0:
                    x = y
                    y = 0
                else:
                    y = -1*(x)
                    x = 0
            else:
                Finalx += x
                Finaly += y
        if [Finalx,Finaly] != [0,0] and x==0 and y==1:
            return False
        return True

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,1
        Finalx = 0
        Finaly = 0
        for action in instructions:
            if action == 'L': 
                x,y = -1*(y),x                 
            elif action == 'R':
                x,y=y,-1*(x)
            else:
                Finalx += x
                Finaly += y
        if [Finalx,Finaly] != [0,0] and x==0 and y==1:
            return False
        return True