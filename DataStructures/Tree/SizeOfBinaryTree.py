def getSize(node):
    x = [0]
    if node:
        def Traverse(node):
            if node:
                x[0] += 1
                if node.left:
                    Traverse(node.left)
                if node.right:
                    Traverse(node.right)
            return
        Traverse(node)
    return(x[0])