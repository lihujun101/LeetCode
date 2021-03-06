class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:

    # 方法：自顶向下
    # 1、根据格式要求，应使用广度搜索，但是广度不大适合递归。这里使用的是先序遍历
    # 2、每次走到根节点，node.left.next = node.right,node.right.next = node.next.left(right到底后，next指向上一个节点的左节点)

    def connect(self, root):
        if not root:
            return None
        elif root.left and root.right:
            root.left.next = root.right
            if root.next:
                if root.next.left :
                    root.right.next = root.next.left

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
    # a5 = TreeNode(5)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.left = a6
    a3.right = a7

    s = Solution()

    m = s.connect(a1)
    print(m)
