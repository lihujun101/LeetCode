class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 删除节点的时候需要考虑这几种情况，父节点为P，子节点为C
    # 1、该节点为叶子节点，原来P->C ，现在P-> None
    # 2、该节点有只有一个子节点，原P->C,现在P->C.left or C.right
    # 3、该节点有两个子节点，原P->C，现在P->C.right.left....left,C.right.left...left ->None

    # 无论如何上面的第一步都是先找父节点

    # 遍历的时候需要去找到该节点的父节点
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if root is None:
            return

        # key所在的位置就是root节点的情况
        if root.val == key:
            if not root.right and not root.left:
                return
            elif not root.right:
                return root.left
            elif root.right:
                min_parent, min_node = self._search_right_min(root.right)
                # 自底向上进行更改关系的绑定
                if min_node.right is None:
                    min_parent.left = None
                else:
                    min_parent.left = min_node.right

                left, right = root.left, root.right
                min_node.left = left
                if min_parent != min_node:
                    min_node.right = right
                return min_node

        # key所在位置不为根节点所在未知的时候
        values = self._search_node(root, key, parent=root)
        if values is None:
            return root
        else:
            parent, leaf, node = values

        # 1、第一种情况
        if not node.left and not node.right:
            if leaf == 'l':
                parent.left = None
            elif leaf == 'r':
                parent.right = None

        # 2、第2种情况，node节点只有一个子节点
        elif node.left is None or node.right is None:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            if leaf == 'l':
                parent.left = node
            elif leaf == 'r':
                parent.right = node

        # 3、第三种情况
        elif node.left and node.right:
            min_parent, min_node = self._search_right_min(node.right)
            # 自底向上进行更改关系的绑定
            if min_node.right is None:
                min_parent.left = None
            else:
                min_parent.left = min_node.right

            if leaf == 'l':
                parent.left = min_node
            elif leaf == 'r':
                parent.right = min_node
            left, right = node.left, node.right
            min_node.left = left
            if min_parent != min_node:
                min_node.right = right

        return root

    # 该方法可以查找到父节点，节点，和节点属于left or right
    def _search_node(self, root, val, parent, leaf=''):
        if root.val == val:
            return parent, leaf, root
        elif root.val > val:
            if root.left:
                return self._search_node(root.left, val, parent=root, leaf='l')
            else:
                return
        else:
            if root.right:
                return self._search_node(root.right, val, parent=root, leaf='r')
            else:
                return

    # 查找右子树的最小值，以及最小值的父节点
    def _search_right_min(self, root):
        parent = root
        while root.left:
            parent = root
            root = root.left
        return parent, root


if __name__ == '__main__':
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node7 = TreeNode(7)

    node5.left = node3
    node5.right = node6
    node3.left = node2
    node3.right = node4
    node6.right = node7
    s = Solution()

    m = s.deleteNode(node5, 3)
    print(m)
