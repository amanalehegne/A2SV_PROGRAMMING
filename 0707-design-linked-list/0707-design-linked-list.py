class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addAtHead(self, val: int) -> None:
        self.count += 1
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def get(self, index: int) -> int:
        if index >= self.count:
            return -1
        head = self.head
        for i in range(index):
            head = head.next

        return head.val

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        if index > self.count:
            return
        if self.count == 0:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif self.count == index:
            self.tail.next = node
            self.tail = node
        else:
            head = self.head
            for i in range(index - 1):
                head = head.next
            nextNode = head.next
            head.next = node
            node.next = nextNode
        self.count += 1

    def addAtTail(self, val: int) -> None:
        self.count += 1
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count or self.count == 0:
            return
        elif index == 0:
            nextNode = self.head.next
            self.head = nextNode
        else:
            head = self.head
            for i in range(index - 1):
                head = head.next
            head.next = head.next.next
            if index == self.count - 1:
                self.tail = head
        self.count -= 1
        if self.count == 0:
            self.head = None
            self.tail = None