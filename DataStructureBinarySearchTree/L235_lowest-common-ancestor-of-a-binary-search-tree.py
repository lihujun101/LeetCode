# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 解题思路：
    # 1、先判断p、q的大小，假设p>q
    # 2、那么p可能在q的右子树；或者p在q的父节点的右子树
    # 3.1、如果p在q的右子树的话，那么q就是最近的公共祖先
    # 3.2  那么从父节点去寻找
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 保证 p.val > q.val，也就是q始终在p的右边
        if p.val < q.val:
            p, q = q, p

        node = root
        nodes = [root]
        # 取出所有的p所有的父节点
        while node:
            if node.val > q.val:
                node = node.left
            elif node.val < q.val:
                node = node.right
            else:
                break
            nodes.append(node)
        # 一个个尝试
        while nodes:
            node = nodes.pop()
            node_0 =node
            while node_0:
                if node_0.val > p.val:
                    node_0 = node_0.left
                elif node_0.val < p.val:
                    node_0 = node_0.right
                else:
                    return node


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node2.left = node1
    node2.right = node3
    node3.right = node4
    s = Solution()
    m = s.lowestCommonAncestor(node2, node1, node3)
    print(m)
