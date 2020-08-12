class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head 
        slow = head
        if not head.next:
            return head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head = slow
        return slow