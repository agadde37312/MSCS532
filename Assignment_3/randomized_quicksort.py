# randomized_quicksort.py
import random
import sys
sys.setrecursionlimit(1000000)

def partition(arr, lo, hi):
    # Lomuto partition
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1

def randomized_partition(arr, lo, hi):
    pivot_index = random.randint(lo, hi)
    arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]
    return partition(arr, lo, hi)

def randomized_quicksort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = randomized_partition(arr, lo, hi)
        randomized_quicksort(arr, lo, p-1)
        randomized_quicksort(arr, p+1, hi)

def deterministic_quicksort(arr, lo=0, hi=None):
    # deterministic pivot: first element
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        # move first element to the end to reuse Lomuto
        arr[lo], arr[hi] = arr[hi], arr[lo]
        p = partition(arr, lo, hi)
        deterministic_quicksort(arr, lo, p-1)
        deterministic_quicksort(arr, p+1, hi)

# Convenience wrappers to avoid modifying original list if not desired
def randomized_quicksort_copy(a):
    b = list(a)
    randomized_quicksort(b)
    return b

def deterministic_quicksort_copy(a):
    b = list(a)
    deterministic_quicksort(b)
    return b
