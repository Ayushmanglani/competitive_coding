class Solution(object):
    def connect(self, root):
        curr = root
        while curr != None:
            head = Node() # dummy head 
            tail = head
            while curr != None:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            curr = head.next
        return root