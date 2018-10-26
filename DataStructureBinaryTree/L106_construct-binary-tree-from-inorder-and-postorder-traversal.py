class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 方法：
    # 1、肯定知道postorder的最后值是主根节点root = node(postorder.pop())
    # 2、last的值在inorder里面是将inorder分为left,right
    # 3、postorder的新的最后一个节点肯定也是一个根节点，这个根节点一定是旧root.left = 新root
    # 4、当右节点全部处理完后，就处理左节点了
    # 5、递归处理
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        node = TreeNode(postorder.pop())
        inorderIndex = inorder.index(node.val)
        node.right = self.buildTree(inorder[inorderIndex + 1:], postorder)
        node.left = self.buildTree(inorder[0:inorderIndex], postorder)

        return node


if __name__ == '__main__':
    s = Solution()
    s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
