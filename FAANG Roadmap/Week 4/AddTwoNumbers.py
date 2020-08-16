class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        while cur1 or cur2:
            if cur1.next and not cur2.next:
                cur2.next = ListNode(0)
            if not cur1.next and cur2.next:
                cur1.next = ListNode(0)
                
            cur2.val += cur1.val
            if cur2.val >= 10:
                if cur1.next:
                    cur1.next.val += (cur2.val//10)
                    cur2.val = (cur2.val%10)
                else:
                    new = ListNode(cur2.val//10)
                    cur1.next = ListNode(0)
                    cur2.next = new
                    cur2.val = (cur2.val%10)
                    
            cur1 = cur1.next
            cur2 = cur2.next
        return l2