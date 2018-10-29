class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 首先该题有2种情况
    # 1、p是q的祖先节点，或者q是p的祖先节点
    # 2、p、q均不互为祖先节点 ，这里可以自顶向下找
    # 2.1 root节点肯定是他们的祖先，我们尝试root.left,root.right是不是祖先，如果是的话继续找，直到不是为止
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # q in p:
        q_node = self._findK(p, q)
        if q_node:
            return p

        # p in q
        p_node = self._findK(q, p)
        if p_node:
            return q
        # p,q in root
        _deque = [root]
        default_left, default_right = True, True
        node = root
        while default_left or default_right:
            default_left, default_right = True, True
            node = _deque.pop()
            if node:
                if node.left:
                    p_node = self._findK(node.left, p)
                    q_node = self._findK(node.left, q)
                    if p_node and q_node:
                        default_left = True
                        _deque.append(node.left)
                    else:
                        default_left = False
                if node.right:
                    p_node = self._findK(node.right, p)
                    q_node = self._findK(node.right, q)
                    if p_node and q_node:
                        default_right = True
                        _deque.append(node.right)
                    else:
                        default_right = False


        return node

    # BFS
    def _findK(self, root, k):
        deque = [root]
        while deque:
            node = deque.pop()
            if node:
                if node == k:
                    return node
                else:
                    if node.left:
                        deque.append(node.left)
                    if node.right:
                        deque.append(node.right)
        return


if __name__ == '__main__':
    a3 = TreeNode(3)
    a5 = TreeNode(5)
    a1 = TreeNode(1)
    a6 = TreeNode(6)
    a2 = TreeNode(2)
    a0 = TreeNode(0)
    a8 = TreeNode(8)
    a7 = TreeNode(7)
   # a4 = TreeNode(4)

    a3.left = a5
    a3.right = a1
    a5.left = a6
    a5.right = a2
    a2.left = a7
    #a2.right = a4
    a1.left = a0
    a1.right = a8

    s = Solution()
    m2 = s.lowestCommonAncestor(a3, a2, a7)
    print(m2.val)
