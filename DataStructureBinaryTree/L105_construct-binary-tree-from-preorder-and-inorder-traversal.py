class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.idx = 0
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 1、可知preorder的第一个数一定是根节点,root=TreeNode(preorder[0])
        # 2、preorder[0] 将 inorder分为left,right
        # 3、新root = TreeNode(preorder[1]) 也一定在left中,root.left = 新root

        if self.idx > len(preorder)-1 or not inorder:
            return
        node = TreeNode(preorder[self.idx])
        self.idx += 1
        inorderIndex = inorder.index(node.val)
        node.left = self.buildTree(preorder, inorder[0:inorderIndex])
        node.right = self.buildTree(preorder, inorder[inorderIndex + 1:])
        return node

if __name__ == '__main__':
    s = Solution()
    node = s.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
    print(node)

