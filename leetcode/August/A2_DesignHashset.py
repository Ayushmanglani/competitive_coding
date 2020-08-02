# Method 1 --> 344ms (Using Binary Search and List as Data Structure) || 17700 kb
import bisect 
class MyHashSet:
    def __init__(self):
        self.hashset = []
        
    def present(self, key: int):
        if self.hashset:
            l = 0
            u = len(self.hashset)-1
            flag = False
            while l<=u:
                mid = l+(u - l)//2
                if self.hashset[mid] == key:
                    flag = True
                    break
                if self.hashset[mid]<key:
                    l = mid+1
                else:
                    u = mid-1
            if flag == True:        
                return mid
            else:
                return -1
        return -1

    def add(self, key: int) -> None:
        if self.present(key) == -1:
            if not self.hashset:
                self.hashset = [key]
            else:
                bisect.insort(self.hashset, key)

    def remove(self, key: int) -> None:
        mid = self.present(key)
        if mid != -1:        
            self.hashset.pop(mid)
            return True
        else:
            return False
        
    def contains(self, key: int) -> bool:
        if self.present(key) != -1:
            return True
        else:
            return False

#Method 2 --> 152 ms (Using Dictionary/Hash) || 18500 kb
class MyHashSet:
    def __init__(self):
        self.hashset = {}

    def add(self, key: int) -> None:
        if key in self.hashset:
            return
        self.hashset[key] = 1

    def remove(self, key: int) -> None:
        if key not in self.hashset:
            return
        del self.hashset[key]
        
    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True