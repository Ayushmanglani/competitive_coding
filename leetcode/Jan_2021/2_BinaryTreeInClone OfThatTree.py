class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        root = cloned
        nodes = [root]
        while nodes:
            curr = nodes.pop()
            if curr.val == target.val:
                return curr
            else:
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        if cloned == None:
            return None
        if target.val == cloned.val:
            return cloned
        return self.getTargetCopy(original, cloned.left, target) or self.getTargetCopy(original, cloned.right, target)