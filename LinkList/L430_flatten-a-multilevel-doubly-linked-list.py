from copy import deepcopy


class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):

    # 自己写的递归方法会失败,想不明白
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
                # 结点的child置为None
                cur.child = None

                cur.next = head_child
                head_child.prev = cur

                # 递归返回的是双链表，并不是双链表的最后一个数
                tail_child = self._flatten(head_child)[1]
                tail_child.next = cur_next
                cur_next.prev = tail_child
            cur = cur_next
            cur_next = cur_next.next
        return head, cur

    # 网上的方法可以通过
    def flatten1(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        while curr:
            if curr.child:
                curr_next = curr.next
                curr.child.prev = curr
                curr.next = curr.child
                last_child = curr
                while last_child.next:
                    last_child = last_child.next
                if curr_next:
                    last_child.next = curr_next
                    curr_next.prev = last_child
                curr.child = None
            curr = curr.next
        return head

    def flatten2(self,head):
        cur = head
        while cur:
            if cur.child is not None:
                cur_next = cur.next
                cur.child.prev = cur
                cur.next = cur.child
                last_child = cur
                # 孩子节点下一个节点不为空的时候，lasr_child往后移动
                while last_child.next is not None:
                    last_child = last_child.next
                # last_child为最后一个孩子节点的时候，需要特殊处理
                if cur_next is not None:
                    last_child.next = cur_next
                    cur_next.prev = last_child
                # 将原有的child置为None
                cur.child = None
            # 这里next是新链表的next
            cur = cur.next
        return head




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

    l1_copy1= deepcopy(l1)
    l1_copy2 = deepcopy(l1)
    s = Solution()
    l2 = s.flatten(l1_copy1)
    l3 = s.flatten2(l1_copy2)

    print(l3 == l1)

    print(l3==l2)
