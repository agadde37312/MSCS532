class Array:
    """
    A simple dynamic array implementation supporting
    insertion, deletion, and indexed access.

    This structure mimics Python's list behavior but
    demonstrates underlying array-based operations.
    """

    def __init__(self):
        self.data = []
        self.length = 0

    def insert(self, value):
        """Insert an element at the end of the array (O(1) amortized)."""
        self.data.append(value)
        self.length += 1

    def delete(self, index):
        """
        Delete an element at a specific index.

        Raises:
            IndexError: if index is out of bounds.

        Time Complexity: O(n) due to shifting.
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        del self.data[index]
        self.length -= 1

    def get(self, index):
        """
        Retrieve the value at a given index.

        Raises:
            IndexError: if the index is not valid.

        Time Complexity: O(1)
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def __len__(self):
        """Return the number of stored elements."""
        return self.length
