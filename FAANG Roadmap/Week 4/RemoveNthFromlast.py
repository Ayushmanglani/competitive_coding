class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        if length == 1:
            return
        target = length - n
        if target == 0:
            head.val = head.next.val
            target = 1
        ptr = head
        curr = head.next
        while target > 1:
            target -= 1
            ptr = ptr.next
            curr = curr.next
        ptr.next = curr.next
        curr.next = None
        return head