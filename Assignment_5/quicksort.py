# quicksort.py
# Deterministic Quicksort using the first element as pivot.

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

    return arr


if __name__ == "__main__":
    test = [8, 4, 7, 3, 2, 9]
    print("Original:", test)
    print("Sorted:", quicksort(test, 0, len(test) - 1))
