class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        pass
        # 假设一样长
        value = 0
        add = 0
        l3 = []
        while l1 or l2:
            if l1 and l2:
                value, add = self._addTwoNumbers(l1.val, l2.val, add)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                value, add = self._addTwoNumbers(l1.val, 0, add)
                l1 = l1.next
            elif l2:
                value, add = self._addTwoNumbers(0, l2.val, add)
                l2 = l2.next
            else:
                value, add = self._addTwoNumbers(0, 0, add)
            l3.append(value)
        print(l3)

    def _addTwoNumbers(self, node1, node2, add=0):

        new_value = node1 + node2 + add

        if new_value < 10:
            return new_value, 0
        else:
            new_value = new_value % 10
            return new_value, 1


if __name__ == '__main__':
    l1 = ListNode(9)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    l2 = ListNode(9)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    m = Solution()
    l3 = m.addTwoNumbers(l1, l2)
    print(l3)
