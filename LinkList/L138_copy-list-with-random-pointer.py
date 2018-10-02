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
        head_copy = RandomListNode(1)
        node_copy = head_copy
        cur = head
        while cur :
            label = cur.label
            node_copy.next = RandomListNode(label)
            node_copy = node_copy.next
            cur = cur.next

        node_copy = head_copy.next
        cur = head
        while cur:
            random = cur.random
            # 指针cur1,node_copy1用于寻找random位置的
            cur1 = head
            node_copy1 = head_copy.next
            if random is not None:
                while cur1 != random:
                    cur1 = cur1.next
                    node_copy1 = node_copy1.next
            else:
                node_copy1 = None
            node_copy.random = node_copy1

            # 处理了一个就同时后移一个单位
            cur = cur.next
            node_copy = node_copy.next

        return head_copy.next







if __name__ == '__main__':
    node1 = RandomListNode(1)
    node1.next = RandomListNode(2)
    node1.next.next = RandomListNode(3)
    node1.next.next.next = RandomListNode(4)
    node1.random = node1.next.next
    s = Solution()
    node2 = s.copyRandomList(node1)
    print(node1)
    print(node2)
