# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# 显然使用广度搜索才对
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        nodes = [root]
        results = []
        if root is None:
            return []
        while nodes:
            result = []
            children_nodes = []
            for node in nodes:
                if node.children:
                    children = node.children
                    for child in children:
                        children_nodes.append(child)
                result.append(node.val)
            nodes = children_nodes
            results.append(result)
        return results
