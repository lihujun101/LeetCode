class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # 这道题适合用后序遍历进行操作，因为是从底部进行比较的
        self.string_list = []
        self.string_dict = {}
        self.dps(root)
        return self.string_list

    # 用字符串作为键
    def dps(self, root):
        if not root:
            return '#'
        if root:
            string = self.dps(root.left) + self.dps(root.right) + str(root.val)
            if string not in self.string_dict:
                self.string_dict[string] = 1
            elif string in self.string_dict and self.string_dict[string] == 1:
                self.string_dict[string] += 1
                self.string_list.append(root)
            return string


if __name__ == '__main__':
    node = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(4)
    node4 = Node(4)
    node5 = Node(4)
    node.left = node1
    node.right = node2
    node1.left = node3
    node2.right = node4
    node4.right = node5
    s = Solution()
    print(s.dps(node))
