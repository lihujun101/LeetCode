import copy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 这是其中一种方法
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nums = []
        lists_copy = []
        for i in range(len(lists)):
            if lists[i] is not None:
                lists_copy.append(lists[i])
        if not lists_copy:
            return
        while lists_copy:
            length = len(lists_copy)
            min_num = float("inf")  # 给定一个无穷大的值
            min_num_row = length  # 行数给定out of index的值
            for i in range(length):
                if min_num > lists_copy[i].val:
                    min_num = lists_copy[i].val
                    min_num_row = i
            if min_num_row == length:
                break
            nums.append(min_num)
            lists_copy[min_num_row] = lists_copy[min_num_row].next
            if lists_copy[min_num_row] is None:  # 某个值为空就和最后一个值交换
                lists_copy[-1], lists_copy[min_num_row] = lists_copy[min_num_row], lists_copy[-1]
                lists_copy.pop()
        return nums


if __name__ == '__main__':
    l0 = ListNode(1)
    l0.next = ListNode(4)
    l0.next.next = ListNode(5)
    l1 = None
    # l1.next = ListNode(3)
    # l1.next = ListNode(4)
    l2 = None
    lists = []
    lists.append(l0)
    lists.append(l1)
    lists.append(l2)
    s = Solution()
    s.mergeKLists(lists)
