class DoublyLinkedListNode(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        newNode = DoublyLinkedListNode(val, None, self.head)
        if self.size == 0:
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        newNode = DoublyLinkedListNode(val, self.tail, None)
        if self.size == 0:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            newNode = DoublyLinkedListNode(val, cur, cur.next)
            cur.next.prev = newNode
            cur.next = newNode
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        self.size -= 1