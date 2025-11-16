# compare_quicksort.py

import random
import time
import matplotlib.pyplot as plt

from quicksort import quicksort
from randomized_quicksort import randomized_quicksort

def measure_time(func, arr):
    start = time.time()
    func(arr.copy(), 0, len(arr) - 1)
    return time.time() - start


def run_experiments():
    sizes = [500, 1000, 2000, 5000, 10000]

    deterministic_times = []
    randomized_times = []

    for n in sizes:
        print(f"Testing input size n = {n}")

        arr = [random.randint(0, 100000) for _ in range(n)]

        deterministic_times.append(measure_time(quicksort, arr))
        randomized_times.append(measure_time(randomized_quicksort, arr))

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, deterministic_times, marker='o', label="Deterministic Quicksort")
    plt.plot(sizes, randomized_times, marker='o', label="Randomized Quicksort")

    plt.title("Quicksort Performance Comparison")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_experiments()
