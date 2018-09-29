class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # 空间复杂度0(n)
        # 双指针
        l3_root = ListNode(None)
        l3 = l3_root

        l1_pointer = l1
        l2_pointer = l2
        while l1_pointer and l2_pointer:
            if l1_pointer.val > l2_pointer.val:
                node = l2_pointer
                l2_pointer = l2_pointer.next
            else:
                node = l1_pointer
                l1_pointer = l1_pointer.next
            l3.next = node
            l3 = l3.next


        if l1_pointer:
            l3.next = l1_pointer
        if l2_pointer:
            l3.next = l2_pointer
        return l3_root.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    l2 = ListNode(2)
    # l2.next = ListNode(4)
    # l2.next.next = ListNode(6)
    s = Solution()
    l3 = s.mergeTwoLists(l1, l2)
    print(l3)
