import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(low):
        return quickselect(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return quickselect(high, k - len(low) - len(equal))
