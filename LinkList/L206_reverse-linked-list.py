class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return
        if head.next is None:
            return head

        # 初始结点
        head0 = head

        # 循环：如果初始结点的下一个节点存在的话就一直循环
        while head0.next is not None:
            # 原头节点
            head_first = head
            # 初始结点的下一个节点
            cur_node_next1 = head0.next
            # 初始结点的下下一个节点
            cur_node_next2 = head0.next.next

            # 初始结点的下一个节点指向原初始结点的下下一个节点
            head0.next = cur_node_next2
            # 原初始节点的下一个节点移动至头结点
            head = cur_node_next1
            # 头节点的下一个节点指向原头节点
            head.next = head_first
        return head


if __name__ == '__main__':
    l1 = ListNode(23)
    l1.next = ListNode(6)
    l1.next.next = ListNode(15)
    s = Solution()
    l2 = s.reverseList(l1)
    print(l2)
