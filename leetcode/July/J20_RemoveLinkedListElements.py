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