class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return None
        prev= ListNode(0,head)
        ans=prev
        curr=head
        nex=head.next
        while nex!=None:
            if curr.val == nex.val and nex!=None:
                while nex!=None and curr.val==nex.val  :
                    nex=nex.next
                prev.next=nex
            else:
                prev=prev.next
            curr=nex
            if nex!=None:
                nex=nex.next
            
        return ans.next