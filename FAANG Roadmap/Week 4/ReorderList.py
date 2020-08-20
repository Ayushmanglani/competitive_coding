class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return head
        slow = head
        fast = head
        prev = head 
        mid = 0
        while fast and fast.next:
            mid += 1
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        def reverse(head):
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
        rev = reverse(slow)
        ptr = head
        prev = head
        while mid > 0:
            mid -= 1
            temp = rev.next
            rev.next = ptr.next
            ptr.next = rev
            prev = ptr.next 
            ptr = ptr.next.next
            rev = temp
        if rev:
            prev.next = rev