#Iterative Approach
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        current = head
        nxt = head.next
        prev = None
        while nxt:
            current.next = prev
            prev = current
            current = nxt
            nxt = nxt.next
        current.next = prev
        head = current
        return head

#Recursive Approach
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rev(prv, cur):
            if not cur:
                return prv
            if cur:
                nxt = cur.next
                cur.next = prv
                return rev(cur, nxt)
        return rev(None, head)        