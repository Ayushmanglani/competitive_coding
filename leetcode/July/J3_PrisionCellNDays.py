class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        d1,d2={tuple(cells):0},{0:tuple(cells)}
        for i in range(1,N+1):
            day=[0]*8
            for j in range(1,7):
                if cells[j-1]==cells[j+1]:
                    day[j]=1
            if tuple(day) in d1:
                k=d1[tuple(day)]
                n=N-i+1
                m=n%(i-k)
                if m==0:
                    return d2[i-1]
                else:
                    return d2[k+m-1]
            d1[tuple(day)]=i
            d2[i]=day
            cells=day
        return day