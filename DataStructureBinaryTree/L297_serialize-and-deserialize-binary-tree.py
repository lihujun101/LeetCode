# Definition for a binary tree node.
import json
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
        # BFS结果展示[1, 2, 3, None, None, 4, 5, None, None, None, None]
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
        return json.dumps(result)

    def deserialize(self, data):
        # [1, 2, 3, None, None, 4, 5, None, None, None, None]转为树结构
        # 1、使用队列做最简单

        data_list = json.loads(data)
        queue = deque()
        index = 0

        root = TreeNode(data_list[index])
        if root.val is None:
            return
        queue.append(root)
        while queue:
            node = queue.popleft()
            for i in ('l', 'r'):
                index += 1
                leaf = TreeNode(data_list[index])
                if leaf.val is not None:
                    if i == 'l':
                        node.left = leaf
                    else:
                        node.right = leaf
                    queue.append(leaf)
        return root


# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(-1)
    a4 = TreeNode(0)
    a5 = TreeNode(1)
    a1.left = a2
    a1.right = a3
    a3.left = a4
    a3.right = a5

    a0 = TreeNode(None)
    codec = Codec()
    m = codec.serialize(a3)
    print(m)
    m1 = codec.deserialize(m)
    print(m1)
