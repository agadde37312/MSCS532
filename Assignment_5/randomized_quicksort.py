# randomized_quicksort.py

import random

def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[low], arr[rand_index] = arr[rand_index], arr[low]
    return deterministic_partition(arr, low, high)


def deterministic_partition(arr, low, high):
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


def randomized_quicksort(arr, low, high):
    if low < high:
        p = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)
    return arr


if __name__ == "__main__":
    test = [8, 4, 7, 3, 2, 9]
    print("Original:", test)
    print("Rand-Sorted:", randomized_quicksort(test, 0, len(test) - 1))
