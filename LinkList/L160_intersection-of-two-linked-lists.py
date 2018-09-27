class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return
        index_max_A,index_max_B = 0,0
        headA0,headB0 = headA,headB
        while headA0 is not None:
            headA0 = headA.next
            index_max_A += 1
        while headB0 is not None:
            headB0 = headB0.next
            index_max_B += 1

        headA0, headB0 = headA, headB
        maxdiff = abs(index_max_A-index_max_B)
        if index_max_A > index_max_B:
            value = 1
            while value <= maxdiff:
                headA0 = headA0.next
                value += 1
        elif index_max_A < index_max_B:
            value = 1
            while value <= maxdiff:
                headB0 = headB0.next
                value += 1
        while headA0 != headB0:
            if headA0 is None or headB0 is None:
                return
            headA0 = headA0.next
            headB0 = headB0.next
        return headA0
