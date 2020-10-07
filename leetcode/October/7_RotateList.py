class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        curr = head
        a = []
        while curr:
            a.append(curr.val)
            curr = curr.next
        l = len(a)
        r = [0]*l
        for i in range(l):
            p = (i+k)%l
            r[p] = a[i] 
        head = ListNode(r[0],None)
        curr = head
        for i in range(1,l):
            new = ListNode(r[i],None)
            curr.next = new
            curr = curr.next
        return(head)