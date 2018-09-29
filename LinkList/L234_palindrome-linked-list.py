class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 双指针做法，一个慢指针，一个快指针，快指针结束的时候，慢指针刚好位于中间位置
    # 慢指针后面的所有数据反转
    # 再给定一个比较指针从头开始和慢指针一一比较

    # 说明：
    # 1、为什么不直接全部反转再一一比较呢？
    # 答：这样的话，空间复杂度就是O(n)，并非O(1)了
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # head = []的情况
        if head is None:
            return True
        # head = [1]的情况
        if head.next is None:
            return True
        # head = [1,2]
        if head.next.next is None:
            if head.next.val == head.val:
                return True
            return False

        slow, fast = head, head.next.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
            # 避免出现fast.next.next的时候，fast.next is None的情况
            if fast is None:
                break
            fast = fast.next

        slow_satrt = slow.next
        # 初始结点
        head0 = slow_satrt
        # 循环：如果初始结点的下一个节点存在的话就一直循环
        while head0.next is not None:
            # 原头节点
            head_first = slow_satrt
            # 初始结点的下一个节点
            cur_node_next1 = head0.next
            # 初始结点的下下一个节点
            cur_node_next2 = head0.next.next

            # 初始结点的下一个节点指向原初始结点的下下一个节点
            head0.next = cur_node_next2
            # 原初始节点的下一个节点移动至头结点
            slow_satrt = cur_node_next1
            # 头节点的下一个节点指向原头节点
            slow_satrt.next = head_first

        slow.next = slow_satrt
        first = head
        second = slow.next
        while second is not None:
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return False
        return True


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(1)
    s = Solution()
    l2 = s.isPalindrome(l1)
    print(l2)
