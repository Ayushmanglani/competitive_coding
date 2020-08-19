class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        
        cur = head.next
        prev = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur.next = None
                cur = prev.next
            else:
                prev = prev.next
                cur = cur.next
        
        while head and head.val == val:
            head = head.next
        return head