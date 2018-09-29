# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


# 违规做法
# from copy import deepcopy
# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: RandomListNode
#         :rtype: RandomListNode
#         """
#         return deepcopy(head)


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        cur = head

        # 复制label
        while cur:
            temp = cur
            cur = cur.next
            copy_node = RandomListNode(temp.label)
            copy_node.next = temp.next
            temp.next = copy_node

        return temp


if __name__ == '__main__':
    node1 = RandomListNode(1)
    node1.next = RandomListNode(2)
    node1.next.next = RandomListNode(3)
    node1.next.next.next = RandomListNode(4)
    s = Solution()
    node2 = s.copyRandomList(node1)
    print(node1)
    print(node2)
