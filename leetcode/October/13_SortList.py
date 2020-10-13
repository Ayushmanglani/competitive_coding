class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        arr = []
        while head is not None:
            arr.append(head)
            head = head.next
        
        arr.sort(key=lambda a: a.val)
        
        for i, a in enumerate(arr):
            if i != len(arr)-1:
                arr[i].next = arr[i+1]
            else:
                arr[i].next = None
        
        return arr[0]

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: #edge case check
            return head
        heap = [] # instantiate an empty list for heapq
        while head: # add all the elements in the linked-list to heapq
            heapq.heappush(heap, head.val)
            head = head.next
            
        newHead = dummy = ListNode(-1)
        while heap: # pop the elements in the heapq and add those to the linkedlist
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next
            
        return newHead.next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None        
        newList=[]
        
        curr = head
        head2 = curr
        
        while head:
            newList.append(head.val)
            head=head.next
            
        newList.sort()
        i=0
        while curr:
            curr.val = newList[i]
            curr = curr.next
            i+=1            
        return head2                