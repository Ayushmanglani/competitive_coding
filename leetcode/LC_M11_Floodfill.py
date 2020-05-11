def col(sr,sc):
    if [sr,sc] not in x:
        img[sr][sc] = nc
        x.append([sr,sc])
        if sr+1<lr and img[sr+1][sc] == oldColor:
            col(sr+1,sc)
        if sc+1<lc and img[sr][sc+1] == oldColor:
            col(sr,sc+1)
        if sr-1>=0 and img[sr-1][sc] == oldColor:
            col(sr-1,sc)
        if sc-1>=0 and img[sr][sc-1] == oldColor:
            col(sr,sc-1)
        return img
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        global lr,lc,oldColor,x,nc,img
        img = image
        nc = newColor
        oldColor = image[sr][sc]
        lr = len(image)
        lc = len(image[0])
        x = []
        return(col(sr,sc))