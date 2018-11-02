# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    # 这道题目的意思就是以迭代器方式依次输出最小值，输出结果就是从小到大的排列
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        while root: # [root,root.left,root.left.left]
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        # 1、__init__里面仅有left节点，且越left的，越是在栈顶[root,root.left,root.left.left]
        # 2、left的值使用掉后，就使用root的值，然后需要加入root.right的值 root.right也是一个子数，所以也从left开始加入
        _min = self.stack.pop()
        right = _min.right
        while right :
            self.stack.append(right)
            right = right.left
        return _min.val




if __name__ == '__main__':
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a2.left = a1
    a2.right = a3

    i, v = BSTIterator(a2), []
    while i.hasNext():
        print(i.next())
