# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    result = []

    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.postorderTraversal1(root.left)
            self.postorderTraversal1(root.right)
            self.result.append(root.val)
        return self.result

    # 这个有个弊端，就是会修改原树结构
    def postorderTraversal2(self, root):
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
                    stack += [node, node.right, node.left]
                    node.right = None
                    node.left = None
                else:
                    result.append(node.val)
        return result

    # 不会修改的原树状结构优化，但是空间复杂度较大
    def postorderTraversal3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        result = []
        node_set = set()
        if root is None:
            return result
        while stack:
            node = stack[-1]
            if node in node_set or (node.left == None and node.right == None):
                node = stack.pop()
                result.append(node.val)
            else:
                node_set.add(node)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result

    # 这个方法比较优，空间复杂度得到保证了，这个方法是网上的
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = [node]
        result = []
        if root is None:
            return result
        while stack:
            n = stack[-1]
            if n.left == node or n.right == node or (n.left == None and n.right == None):
                node = stack.pop()
                result.append(node.val)
            else:
                if n.right:
                    stack.append(n.right)
                if n.left:
                    stack.append(n.left)
        return result


if __name__ == '__main__':
    a0 = TreeNode(0)
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)

    a0.left = a1
    a0.right = a2
    a1.left = a3
    a1.right = a4
    a4.right = a5
    s = Solution()

    print(s.postorderTraversal(a0))
