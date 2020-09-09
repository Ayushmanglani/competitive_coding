class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:        
        i = 0
        v1 = version1.split(".")
        v2 = version2.split(".")
        l1 = len(v1)
        l2 = len(v2)
        print(v1,v2)
        while i<l1 or i<l2:
            if i>=l1 and i<l2:
                if int(v2[i]) == 0:
                    i += 1
                    continue
                else:
                    return -1
            elif i>=l2 and i<l1:
                if int(v1[i]) == 0:
                    i += 1
                    continue
                else:
                    return 1
            else:
                if int(v1[i]) > int(v2[i]):
                    return 1
                elif int(v1[i]) < int(v2[i]):
                    return -1
            i += 1
        return 0


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=list(map(int,version1.split('.'))) #Splitting version at '.' and converting each part to int
        version2=list(map(int,version2.split('.')))
        n=len(version1)
        m=len(version2)
        if(n>m):                      #To make length of both version equal
            for i in range(n-m):
                version2.append(0)
        else:
            for i in range(m-n):
                version1.append(0)

        for i in range(len(version1)):   #Final Comparision
            if(version1[i]>version2[i]):
                return 1
            if(version1[i]<version2[i]):
                return -1
        return 0        