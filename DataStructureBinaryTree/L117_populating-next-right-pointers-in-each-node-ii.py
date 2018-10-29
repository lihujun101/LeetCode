class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:

    # 看题适合自顶向下的做法
    def connect(self, root, start=None, begin=None):
        if not root:
            return None

        if root.left or root.right:  # root非叶子节点，需要确定start的位置和下一层的位置
            if start:
                if root.left and root.right:
                    start.next = root.left
                    root.left.next = root.right
                    start = root.right
                elif root.left:
                    start.next = root.left
                    start = start.next
                else:
                    start.next = root.right
                    start = start.next
            else:
                if root.left and root.right:
                    root.left.next = root.right
                    start = root.right
                elif root.left:
                    start = root.left
                else:
                    start = root.right

                if root.left:
                    begin = root.left
                elif root.right:
                    begin = root.right
            self.connect(root.next, start)

        else:  # root为叶子节点
            self.connect(root.next, start)
            if begin:
                begin = begin.next

        if begin:
            self.connect(begin, start=None)


if __name__ == '__main__':
    # a1 = TreeLinkNode(1)
    # a2 = TreeLinkNode(2)
    # a3 = TreeLinkNode(3)
    # a4 = TreeLinkNode(4)
    # a5 = TreeLinkNode(5)
    # a6 = TreeLinkNode(6)
    # a7 = TreeLinkNode(7)
    # a8 = TreeLinkNode(8)
    #
    # a1.left = a2
    # a1.right = a3
    # a2.left = a4
    # a2.right = a5
    # # a3.left = a6
    # a3.right = a6
    # a4.left = a7
    # a6.right = a8
    # a1_0 = TreeLinkNode(0)
    # a2_2 = TreeLinkNode(2)
    # a2_4 = TreeLinkNode(4)
    # a3_1 = TreeLinkNode(1)
    # a3_3 = TreeLinkNode(3)
    # a3_p1 = TreeLinkNode(-1)
    # a4_5 = TreeLinkNode(5)
    # a4_1 = TreeLinkNode(1)
    # a4_6 = TreeLinkNode(6)
    # a4_8 = TreeLinkNode(8)
    # a1_0.left = a2_2
    # a1_0.right = a2_4
    # a2_2.left = a3_1
    # a2_4.left = a3_3
    # a2_4.right = a3_p1
    # a3_1.left = a4_5
    # a3_1.right = a4_1
    # a3_3.right = a4_6
    # a3_p1.right = a4_8
    a1_1 = TreeLinkNode(1)
    a2_1 = TreeLinkNode(2)
    a2_2 = TreeLinkNode(2)
    a3_1 = TreeLinkNode(3)
    a3_2 = TreeLinkNode(3)
    a4_1 = TreeLinkNode(4)
    a4_2 = TreeLinkNode(5)
    a1_1.left = a2_1
    a1_1.right = a2_2
    a2_1.left = a3_1
    a2_2.right = a3_2
    a3_1.left = a4_1
    a3_1.right = a4_2

    s = Solution()

    m = s.connect(a1_1)
    print(m)
