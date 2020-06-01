# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            k = 0      
            current = head
            currentlast = 0
            while current:
                k += 1
                currentlast = current
                current = current.next
            i = 2
            # print(k)
            if head.next:
                current = head.next
                currentprev = head
                if current == currentlast:
                    return head
                while i<=k:
                    if i%2 == 0:
                        currentprev.next = current.next                
                        currentlast.next = current
                        currentlast = current
                        currentlast.next = None 
                    else:
                        currentprev = currentprev.next 
                    i += 1
                    current = currentprev.next
            return(head)
        return