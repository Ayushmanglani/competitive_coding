class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        while cur:
            pre.val, cur.val = cur.val, pre.val
            pre = cur.next
            if not pre:
                break    
            cur = pre.next            
        return head

class Solution(object):
    def swapPairs(self, head):
        temp = ListNode(0)
        temp1 = temp
        temp.next = head
        
        while temp.next and temp.next.next:
            node1 = temp.next.next
            node2 = temp.next
            node3 = temp.next.next.next
            
            temp.next = node1
            temp.next.next = node2
            temp.next.next.next = node3
        
            temp = temp.next.next
        
        return temp1.next        