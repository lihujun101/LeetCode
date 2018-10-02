class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    s = Solution()
    node2 = s.rotateRight(node1,2)
    print(node2)

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return
        if head.next is None:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # 正序应该在的位置
        k1 = length - k % length


        if k1 == length:
            return head
        # 1 2 3 4 5，假设k = 2,k1 =5-2 =3
        cur = head
        while k1 > 1:
            cur = cur.next
            k1 -= 1
        # 头结点，分开前后的结点
        head0 = head
        next = cur.next
        cur.next = None
        head = next
        next_node = next
        while next_node.next:
            next_node = next_node.next

        next_node.next = head0
        return head
