class Codec:

    def serialize(self, root: TreeNode) -> str:
        if root == None:
            return "$"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        

    def deserialize(self, data: str) -> TreeNode:
        nodes = data.split(",")
        self.i = 0
        def dfs():
            if self.i == len(nodes) or nodes[self.i] == "$":
                self.i += 1
                return None
            root = TreeNode(int(nodes[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
        

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def preorder(root):
            if not root:
                return None
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ' '.join(map(str, res))
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        inputs = data.split()
        inputs = list(map(int, inputs))
        def build(minv,maxv):
            if inputs and minv < inputs[0] < maxv:
                v = inputs.pop(0)
                root = TreeNode(v)
                root.left = build(minv, v)
                root.right = build(v, maxv)
                return root
        
        node = build(float('-inf'), float('inf'))
        return node        