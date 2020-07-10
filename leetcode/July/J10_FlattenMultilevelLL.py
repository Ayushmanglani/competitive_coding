class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        order = []
        def traverse(curr):
            order.append(curr)
            if curr.child:
                traverse(curr.child)
            if curr.next:
                traverse(curr.next)
        curr = head
        traverse(curr)
        # print(order)
        
        for i in range(len(order) - 1):
            order[i].child = None
            order[i + 1].child = None
            order[i].next = order[i + 1]
            order[i + 1].prev = order[i]
        return order[0]
'''
Method 2

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        parent_stack = []
        
        old_head = head
        
        while head.next or head.child or len(parent_stack):
            if not head.next and not head.child:
                head.next = parent_stack.pop()
                head.next.prev = head
            elif head.child:
                if head.next:
                    parent_stack.append(head.next)
                head.next = head.child
                head.child.prev = head
            head.child = None
            head = head.next
        
        return old_head