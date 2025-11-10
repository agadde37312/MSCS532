# priority_queue.py

class Task:
    """A simple Task object with an ID and priority."""
    def __init__(self, task_id, priority, arrival_time=None, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"


class PriorityQueue:
    """Max-heap based priority queue."""
    def __init__(self):
        self.heap = []

    def parent(self, i): return (i - 1) // 2
    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2

    def insert(self, task):
        """Insert new task into the heap."""
        self.heap.append(task)
        idx = len(self.heap) - 1

        # Bubble up
        while idx != 0 and self.heap[self.parent(idx)].priority < self.heap[idx].priority:
            p = self.parent(idx)
            self.heap[idx], self.heap[p] = self.heap[p], self.heap[idx]
            idx = p

    def extract_max(self):
        """Remove and return max-priority task."""
        if self.is_empty():
            return None

        root = self.heap[0]
        last = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last
            self.heapify(0)

        return root

    def heapify(self, i):
        """Restore heap property from index i."""
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def increase_priority(self, task_id, new_priority):
        """Increase priority and fix heap."""
        for i in range(len(self.heap)):
            if self.heap[i].task_id == task_id:
                self.heap[i].priority = new_priority

                # Bubble up
                while i != 0 and self.heap[self.parent(i)].priority < self.heap[i].priority:
                    p = self.parent(i)
                    self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                    i = p
                return True
        return False

    def is_empty(self):
        return len(self.heap) == 0


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task("A", 3))
    pq.insert(Task("B", 5))
    pq.insert(Task("C", 1))

    print("Extracted:", pq.extract_max())
    print("Remaining heap:", pq.heap)
