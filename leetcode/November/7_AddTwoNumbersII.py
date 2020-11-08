class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a1 = []
        a2 = []
        n1 = 0
        n2 = 0
        cur1 = l1
        cur2 = l2
        while cur1:
            a1.append(cur1.val)
            cur1 = cur1.next
            n1 += 1
        while cur2:
            a2.append(cur2.val)
            cur2 = cur2.next            
            n2 += 1
        if n1>n2:
            a2 = [0]*(n1-n2) + a2
            cur1 = l1
        else:
            a1 = [0]*(n2-n1) + a1 
            cur1 = l2
        extra = False            
        for i in range(max(n1,n2)-1,-1,-1):
            a1[i] += a2[i]
            if a1[i]>=10:
                a1[i] -= 10
                if i != 0:                    
                    a1[i-1] += 1
                else:
                    extra = True
                    a1 = [1]+a1
        i = 0
        while cur1.next:
            cur1.val = a1[i]
            cur1 = cur1.next
            i+=1
        cur1.val = a1[i] 
        if extra:
            new = ListNode()
            new.val = a1[i+1]
            cur1.next = new
            
        if n1>n2:
            return l1
        return l2