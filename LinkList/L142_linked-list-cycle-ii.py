class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        recode_nodes = set()
        if head is None or head.next is None:
            return
        while head not in recode_nodes:
            recode_nodes.add(head)
            if head.next is None:
                return
            head = head.next
        return head
