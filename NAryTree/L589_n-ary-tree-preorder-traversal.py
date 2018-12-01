
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return
        queue = [root]
        result = []
        while queue:
            node = queue.pop()
            result.append(node.val)
            if node.children:
                children = node.children
                while children:
                    child = children.pop()
                    queue.append(child)
        return result

