class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = l2 = 0
        cur = headA
        while cur:
            l1 += 1
            cur = cur.next
        cur = headB
        while cur:
            l2 += 1
            cur = cur.next
        if l1 == 0 or l2 == 0:
            return
        if l1 > l2:
            d = l1-l2
            while d>0:
                headA = headA.next
                d -= 1
        elif l1 < l2:
            d = l2-l1
            while d>0:
                headB = headB.next
                d -= 1
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None