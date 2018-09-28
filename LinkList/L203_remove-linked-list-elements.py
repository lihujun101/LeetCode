class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 从第一个结点进行判断，如果第一个值满足就往后移动
        while head and head.val == val:
            head = head.next

        if head is None:
            return
        else:
            # 非头结点满足的情况下，往后移动
            cur = head
            while cur.next is not None:
                head0 = cur.next
                if head0.val == val:
                    cur.next = head0.next
                else:
                    cur = cur.next

            return head


if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)
    s = Solution()
    l2 = s.removeElements(l1, 1)
    print(l2)
