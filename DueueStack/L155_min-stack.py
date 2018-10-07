# class Node:
#     def __init__(self, x, next=None):
#         self.x = x
#         self.next = next
#
# class MinStack:
#     # 通过链表去实现，1->2->3，1就是栈顶
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self._head = None
#         self.length = 0
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.length += 1
#         node = Node(x)
#         head = self._head
#         node.next = head
#         self._head = node
#
#     def pop(self):
#         """
#         :rtype: void
#         """
#
#         if self._head is None:
#             raise Exception('None stack')
#         self.length -= 1
#         head = self._head
#         self._head = self._head.next
#         return head.x
#
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         if self._head is None:
#             return None
#         head = self._head
#         return head.x
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         if self._head is None:
#             return
#         head = self._head
#         min_value = head.x
#         while head :
#             if min_value > head.x:
#                 min_value = head.x
#             head = head.next
#         return min_value

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self._min:
            self._stack.append(0)
            self._min = x
        else:
            x1 = x - self._min
            self._stack.append(x1)
            if x1 < 0:
                self._min = x

    def pop(self):
        """
        :rtype: void
        """
        x1 = self._stack.pop()
        if x1 < 0:
            self._min = self._min - x1

    def top(self):
        """
        :rtype: int
        """
        x = self._stack[-1]
        if x > 0:
            return x + self._min
        else:
            return self._min

    def getMin(self):
        """
        :rtype: int
        """
        return self._min


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
