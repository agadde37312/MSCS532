# Course: MSCS532
# Assignment 1: Insertion Sort (Monotonically Decreasing Order)

def insertion_sort_desc(arr):
    """
    Performs insertion sort on the input list in decreasing order.
    :param arr: list of numbers to sort
    :return: sorted list (in-place)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Moving elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    # Example usage
    num = [2, 5, 0, 3, 9]
    print("Original array:", num)
    insertion_sort_desc(num)
    print("Sorted array (decreasing order):", num)
