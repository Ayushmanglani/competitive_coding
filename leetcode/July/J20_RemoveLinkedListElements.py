class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        while start.next:
            if start.next.val == val:
                start.next = start.next.next
            else:
                start = start.next         
        return dummy.next

#Method 2
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head:
            ptr = head
            if ptr.next:
                current = ptr.next
                while current:
                    if current.val == val:
                        ptr.next = current.next  
                        current.next = None
                        current = ptr.next
                    else:
                        current = current.next
                        ptr = ptr.next
            if head.val == val:
                head = head.next
            return head