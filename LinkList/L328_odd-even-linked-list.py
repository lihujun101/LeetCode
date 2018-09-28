class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        if head.next is None or head.next.next is None:
            return head

        # 双指针,i位置在最新奇数位置，j每次移动2格,prev_j是j前一个位置
        i,prev_j,j = head,head.next,head.next.next
        while True:
            node_j = j
            next_i = i.next
            if j.next is None:
                i.next = node_j
                prev_j.next = None
                node_j.next = next_i
                break
            elif j.next.next is None:
                i.next = node_j
                prev_j.next = node_j.next
                node_j.next = next_i
                break
            else:
                # 位置交换
                # 1 -> 2 -> 3 -> 4,i表示1,next_i表示2，node_j表示3
                # i(1).next = node_j(3),prev_j(2).next = node_j.next(4),node_j(3).next = next_i(2)
                # 1 -> 3 -> 2 -> 4

                # 先交换一部分
                i.next = node_j
                prev_j.next = node_j.next

                # 位置交换前，j先移动2位，不然交换后移动的话位置会变
                prev_j = j.next
                j = prev_j.next

                # j移动位置后再进行交换
                node_j.next = next_i
                i = node_j
        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next.next = ListNode(7)

    s = Solution()
    l2 = s.oddEvenList(l1)
    print(l2)
