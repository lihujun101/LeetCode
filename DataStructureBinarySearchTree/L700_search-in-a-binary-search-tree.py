class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val > val:
            return self.searchBST(root.left,val)
        elif root.val < val:
            return self.searchBST(root.right,val)
        else:
            return root

if __name__ == '__main__':
    node = TreeNode(0)
    node1 = TreeNode(1)
    node.right = node1

    del node
    print(node)