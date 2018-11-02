class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root = TreeNode(val)
            return root
        if val > root.val :
            if root.right:
                self.insertIntoBST(root.right,val)
            else:
                root.right = TreeNode(val)
        elif val < root.val:
            if root.left :
                self.insertIntoBST(root.left,val)
            else:
                root.left =  TreeNode(val)
        return root
