class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        boolval = False
        node = head
        while node is not None :
            node = node.next
            if node == head:
                boolval = True
                break
            elif node is None:
                break
        return boolval


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
   # node1.next.next.next = node1
    print(1)
    s = Solution()
    s1 = s.hasCycle(node1)
    print(s1)
