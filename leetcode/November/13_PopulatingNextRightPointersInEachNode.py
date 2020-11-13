class Solution(object):
    def connect(self, root):
        ## bsf
        if not root:
            return None
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)
        return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        cache = []  # At most with size == height of tree

        def connect(root, depth):
            if root is None:
                return
            if len(cache) <= depth:
                cache.append(root)
            else:
                cache[depth].next = root
                cache[depth] = root
            connect(root.left, depth+1)
            connect(root.right, depth+1)

        connect(root, 0)
        return root