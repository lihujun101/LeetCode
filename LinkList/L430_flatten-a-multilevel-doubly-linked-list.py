class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return
        if head.next is None:
            return head
        return self._flatten(head)[0]

    def _flatten(self, head):
        cur = head
        cur_next = head
        while cur.next is not None:
            if cur.child is not None:
                # 更换之前需要记录cur_next的位置
                cur_next = cur.next
                head_child = cur.child
                cur.next = head_child
                head_child.prev = cur
                # 递归返回的是双链表，并不是双链表的最后一个数
                tail_child = self._flatten(head_child)[1]
                tail_child.next = cur_next
                cur_next.prev = tail_child
            cur = cur_next
            cur_next = cur_next.next
        return head, cur


if __name__ == '__main__':
    l3 = Node(11)
    node_0 = l3
    for i in range(12, 13):
        node = Node(i)
        node_0.next = node
        node.prev = node_0
        node_0 = node

    # 构造一组双端列表
    l2 = Node(7)
    node_0 = l2
    for i in range(8, 11):
        node = Node(i)
        node_0.next = node
        node.prev = node_0
        node_0 = node
        if i == 8:
            node.child = l3

    l1 = Node(1)
    node_0 = l1
    for i in range(2, 7):
        node = Node(i)
        node_0.next = node
        node.prev = node_0
        node_0 = node
        if i == 3:
            node.child = l2
    s = Solution()
    l1 = s.flatten(l1)
    print(l1)
