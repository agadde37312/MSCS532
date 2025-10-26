# Assignment 1: Insertion Sort (Monotonically Decreasing Order)
#updating for third commit of the file

def insertion_sort_desc(arr):
    """
    Performs insertion sort on the input list in decreasing order.
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
    num = [12,15, 20, 3, 19]
    print("Original array:", num)
    insertion_sort_desc(num)
    print("Sorted array (decreasing order):", num)
