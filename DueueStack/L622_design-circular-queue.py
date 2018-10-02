class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MyCircularQueue:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.max_length = k
        self.length = 0
        self._items = None
        self.head = None
        self.tail = None

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.length >= self.max_length:
            return False
        node = Node(value)
        self.length += 1
        if self.head is None:
            self._items = node
            self.head = self._items
            self.tail = self._items
        else:
            tail_node = self.tail
            self.tail = node
            tail_node.next = self.tail
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.length <= 0:
            return False
        self.length -= 1

        self.head = self.head.next
        self._items = self.head
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self._items is None:
            return -1
        return self.head.value

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self._items is None:
            return -1
        return self.tail.value

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.length == 0:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.length == self.max_length:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
if __name__ == '__main__':
    l1 = Node(1)
    s = MyCircularQueue(3)
    print(s.enQueue(1))
    print(s.enQueue(2))
    print(s.enQueue(3))
    print(s.enQueue(4))
    print(s.Rear())
    print(s.isFull())
    print(s.deQueue())
    print(s.enQueue(4))
    print(s.Rear())
