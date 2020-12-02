class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val

import random
class Solution(object):
    def __init__(self, head):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self):
        return random.choice(self.arr)        