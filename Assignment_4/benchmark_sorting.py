# benchmark_sorting.py

import random
import time
import matplotlib.pyplot as plt
from heapsort import heapsort

# Built-in python sorts
def mergesort_test(arr): return sorted(arr)
def quicksort_test(arr): return sorted(arr)

def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    return time.time() - start


def run_benchmarks():
    sizes = [500, 1000, 2000, 5000, 10000]
    heap_times = []
    quick_times = []
    merge_times = []

    for n in sizes:
        arr = [random.randint(0, 100000) for _ in range(n)]
        print(f"Testing n = {n}")

        heap_times.append(measure_time(heapsort, arr))
        quick_times.append(measure_time(quicksort_test, arr))
        merge_times.append(measure_time(mergesort_test, arr))

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, heap_times, marker='o', label="Heapsort")
    plt.plot(sizes, quick_times, marker='o', label="Quicksort (Python)")
    plt.plot(sizes, merge_times, marker='o', label="Merge Sort (Python)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Benchmark Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_benchmarks()
