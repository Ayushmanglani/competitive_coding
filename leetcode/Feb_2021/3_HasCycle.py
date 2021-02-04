class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True        
        return False

class Solution(object):
    def hasCycle(self, head):
        cur = head
        while cur:
            if cur.val == 'C':
                return True
            cur.val = 'C'
            cur = cur.next
        return False        