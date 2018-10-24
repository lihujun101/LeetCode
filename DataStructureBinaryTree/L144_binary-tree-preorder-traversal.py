class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归方式
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is not None:
            print(root.val)
            self.preorderTraversal1(root.left)
            self.preorderTraversal1(root.right)


    # 非递归算法
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                if node.left or node.right:
                    stack += [node.right,node.left,node]
                    node.right = None
                    node.left = None
                else:
                    result.append(node.val)

        return result


if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    print(s.preorderTraversal(node1))
