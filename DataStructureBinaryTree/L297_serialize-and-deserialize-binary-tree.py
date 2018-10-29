# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 采用BFS搜索,采用队列
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            node = queue.popleft()
            if node:
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
                result.append(node.val)
            else:
                result.append(node)

        return str(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.strip('[]').split(',')
        # 可采用双指针，一个指向根，一个指向left、right
        index = 0
        leaf_min = 1
        max_length = len(data_list) - 1
        level = 1
        while leaf_min < max_length:
            leaf_min = 2 ** level - 1
            level_max = 2 ** (level + 1) - 1
            root_val = data_list[index]
            root = TreeNode(root_val)
            m = -1
            for i in range(leaf_min, level_max + 1):
                if m == -1:
                    left = TreeNode(data_list[i])
                    m = 1
                    root.left = left
                else:
                    right = TreeNode(data_list[i])
                    m = -1
                    root.right = right


        # Your Codec object will be instantiated and called as such:


# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)
    a1.left = a2
    a1.right = a3
    a3.left = a4
    a3.right = a5
    codec = Codec()
    print(codec.serialize(a1))
