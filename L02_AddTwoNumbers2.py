class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l3 = []
        value2 = 0
        value1 = 0
        while l1 or l2:
            value1, value2 = self._addTwoNumbers(l1.val, l2.val, value2)
            l3.append(value1)
            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1 = l1.next
                l2 = 0
            elif l2:
                l1 = 0
                l2 = l2.next

        if [value1,value2] == [0,1]:
            l3.append(value2)
        return l3

    def _addTwoNumbers(self, node1, node2, value=0):
        '''
        :param node1:第1个数
        :param node2:第2个数
        :param value:是否需要向上进制1位
        :return:返回相加后的余数，以及是否需要向前进制
        '''
        new_value = node1 + node2 + value
        if new_value < 10:
            return new_value, value
        else:
            new_value = new_value % 10
            value = 1
            return new_value, value


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    m = Solution()
    l3 = m.addTwoNumbers(l1, l2)
    print(l3)
