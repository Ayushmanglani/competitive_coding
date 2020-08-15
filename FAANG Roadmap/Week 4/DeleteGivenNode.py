class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        addr = node.next.next
        node.next.next = None
        node.next = addr