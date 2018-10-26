class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:

    # 方法：
    # 1、根据格式要求，应使用广度搜索
    # 2、每次走到根节点，就有一个next指向下一个根节点

    def connect(self, root):
        pass

    def change(self, root):
        if root:
            pre = root
            node = root



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

    m = s.change(a1)
    print(m)
