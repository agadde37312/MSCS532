class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.data:
            raise IndexError("Queue is empty")
        return self.data.pop(0)
