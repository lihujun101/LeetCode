class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):
    # root->Node(1)->Node(2)
    def __init__(self):
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def get(self, index):
        if index >= 0 and index <= self.length - 1:
            node = self.root.next
            idx = 0
            while idx < index:
                node = node.next
                idx += 1
            return node.val
        else:
            return -1

    def addAtHead(self, val):
        self.length += 1
        head = self.root.next
        # 把tailnode节点位置找到
        node = Node(val)
        if head is None:
            self.tailnode = node
        self.root.next = node
        node.next = head

    def addAtTail(self, val):
        tailnode = self.tailnode
        if tailnode is None:
            return self.addAtHead(val)
        self.length += 1
        node = Node(val)
        tailnode.next = node
        self.tailnode = node

    def addAtIndex(self, index, val):
        if index == self.length:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)
        if index > 0 and index < self.length:
            self.length += 1
            node = self.root.next
            node_insert = Node(val)
            cur = node
            idx = 0
            while idx < index:
                cur = node
                node = node.next
                idx += 1
            cur.next = node_insert
            node_insert.next = node

    def deleteAtIndex(self, index):
        if index > 0 and index < self.length - 1:
            self.length -= 1
            node = self.root.next
            idx = 0
            cur = node
            while idx < index:
                cur = node
                node = node.next
                idx += 1
            value = node.val
            cur.next = node.next
            del node
            return value
        elif index == self.length - 1:
            self.length -= 1
            node = self.root.next
            idx = 0
            cur = node
            while idx < index:
                cur = node
                node = node.next
                idx += 1
            value = node.val
            cur.next = None
            self.tailnode = cur
            del node
            return value
        elif index == 0:
            self.length -= 1
            node = self.root.next
            self.root.next = node.next
            value = node.val
            del node
            return value


if __name__ == '__main__':
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)

    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    linkedList.deleteAtIndex(2)

    print(linkedList.get(0))
