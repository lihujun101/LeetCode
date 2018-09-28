class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 两次遍历
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        length = 0
        head_0 = head
        # 链表长度
        while head_0 is not None:
            head_0 = head_0.next
            length += 1

        # 正序的位置
        idx_n = length - n
        # 排序为0
        if idx_n == 0:
            head = head.next
            return head

        head_0, cur, idx = head, head_0, 0
        while idx < idx_n:
            cur, head_0 = head_0, head_0.next
            idx += 1
        if head_0 is None:
            cur.next = None

        else:
            cur.next = head_0.next
        del head_0
        return head

    # 一次遍历，两个指针差值为n
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        idx = 0
        head_i, head_j = head, head
        while idx < n:
            head_j = head_j.next
            idx += 1
        # 如果n为第一个节点的话，需特殊处理
        if head_j is None:
            head = head.next
            return head
        # 当head_j.next指向None的时候，head_i.next就是倒数第n个值
        while head_j.next is not None:
            head_i = head_i.next
            head_j = head_j.next
        cur = head_i.next
        head_i.next = cur.next
        del cur
        return head


if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    s = Solution()
    l2 = (s.removeNthFromEnd(l1,5))
    print(l2)
