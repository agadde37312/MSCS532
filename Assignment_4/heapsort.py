# heapsort.py

def heapify(arr, n, i):
    """Fixes the heap at index i for a max-heap."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    """Sorts an array using max-heap."""
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move max to end
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    test = [4, 10, 3, 5, 1]
    print("Original:", test)
    print("Heapsorted:", heapsort(test))
