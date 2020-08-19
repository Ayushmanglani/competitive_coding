class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head.next:
            return head
        cur = head
        #Reverse section in LL
        def rev(prv, curr):
            if not curr:
                return prv
            if curr:
                nxt = curr.next
                curr.next = prv
                return rev(curr, nxt)
            return rev(None, head)  
        prevv = None
        while cur:
            p = k-2

            #Going till end of each section of k nodes
            ptr = cur.next
            while ptr and p>0:
                p -= 1
                ptr = ptr.next
            if p != 0 or not ptr:
                break

            tem = ptr.next # Storing address of next Node

            ptr.next = None #removing next nodes to get one group of nodes

            cur = rev(None,cur) #Reversed group of nodes

            #Assigning reversed node head address to its previous node of LL
            if prevv == None: 
                head = cur
            else:
                prevv.next = cur

            #Going till end of reverse Linked list
            ptr = cur
            while ptr.next != None:
                ptr = ptr.next

            ptr.next = tem #Adding next nodes
            prevv = ptr #storing Previous node for next group
            cur = ptr.next
        return(head)