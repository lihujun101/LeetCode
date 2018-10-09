from collections import deque


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.popleft()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0

if __name__ == '__main__':
    que = MyQueue()
    que.push(1)
    que.push(2)
    print(que.peek())
    print(que.pop())
    print(que.empty())

