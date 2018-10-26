class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:

    def connect(self, root):
        if not root:
            return None

        if root.left and root.right:
            root.left.next = root.right
            current = root.right
        elif root.left:
            current = root.left
        elif root.right:
            current = root.right
        else:  # 该节点是叶子节点
            current = None

        if current is not None:
            if root.next:
                if root.next.left:
                    current.next = root.next.left
                elif root.next.right:
                    current.next = root.next.right

            self.connect(root.left)
            self.connect(root.right)




if __name__ == '__main__':
    a1 = TreeLinkNode(1)
    a2 = TreeLinkNode(2)
    a3 = TreeLinkNode(3)
    a4 = TreeLinkNode(4)
    a5 = TreeLinkNode(5)
    a6 = TreeLinkNode(6)
    a7 = TreeLinkNode(7)
    a8 = TreeLinkNode(8)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    # a3.left = a6
    a3.right = a6
    a4.left = a7
    a6.right = a8

    s = Solution()

    m = s.connect(a1)
    print(m)
