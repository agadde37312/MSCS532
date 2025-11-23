class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def delete_value(self, value):
        if not self.head:
            return
        if self.head.val == value:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.val != value:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def traverse(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
