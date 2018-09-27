class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 想不明白为什么超时了，O(n)时间复杂度
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         boolval = False
#         node = head
#         while node is not None :
#             node = node.next
#             if node == head:
#                 boolval = True
#                 break
#             elif node is None:
#                 break
#         return boolval


# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         boolval = False
#         node = head
#         while node is not None :
#             node = node.next
#             if node == head:
#                 boolval = True
#                 break
#             elif node is None:
#                 break
#         return boolval


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if slow is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next

            if fast.next is None:
                return False
            fast = fast.next
        return True


if __name__ == '__main__':
    node1 = ListNode(3)
    node1.next = ListNode(2)
    node1.next.next = ListNode(0)
    node1.next.next.next = ListNode(-4)
   # node1.next.next.next = node1
    print(1)
    s = Solution()
    s1 = s.hasCycle(node1)
    print(s1)
