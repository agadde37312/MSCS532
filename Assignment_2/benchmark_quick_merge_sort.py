"""
Benchmarking Quick Sort vs Merge Sort
--------------------------------------
Author: Arun Bhaskar Gadde
Course: 2025 Fall - Algorithms and Data Structures (MSCS-532-B01) - Second Bi-term
Assignment 2 - Analyzing and Implementing Divide-and-Conquer Algorithms

This script compares Quick Sort and Merge Sort using:
- Sorted, reverse sorted, and random datasets
- Execution time (milliseconds)
- Memory usage (KB)
"""

import random
import time
import tracemalloc
import pandas as pd

# -------------------------------
# Quick Sort Implementation
# -------------------------------
def quick_sort(arr):
    """Performs Quick Sort in descending order."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]  # descending order
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quick_sort(left) + middle + quick_sort(right)

# -------------------------------
# Merge Sort Implementation
# -------------------------------
def merge_sort(arr):
    """Performs Merge Sort in descending order."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Helper function to merge two sorted lists."""
    result = []
    while left and right:
        if left[0] > right[0]:  # descending order
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

# -------------------------------
# Benchmarking Function
# -------------------------------
def benchmark_algorithm(sort_func, dataset):
    """Measures execution time and memory usage."""
    tracemalloc.start()
    start_time = time.perf_counter()
    sort_func(dataset.copy())
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    exec_time_ms = (end_time - start_time) * 1000
    memory_kb = peak / 1024
    return exec_time_ms, memory_kb

# -------------------------------
# Dataset Generation
# -------------------------------
def generate_datasets(size=10000):
    """Generates datasets of various types."""
    sorted_data = list(range(size, 0, -1))  # already sorted descending
    reverse_data = list(range(1, size + 1))  # ascending (worst for Quick Sort)
    random_data = random.sample(range(size * 2), size)
    return {
        "Sorted": sorted_data,
        "Reverse": reverse_data,
        "Random": random_data
    }

# -------------------------------
# Main Execution
# -------------------------------
def main():
    datasets = generate_datasets(7000)  # you can increase to 10,000 for deeper testing
    results = []

    for name, data in datasets.items():
        for algo_name, func in [("Quick Sort", quick_sort), ("Merge Sort", merge_sort)]:
            exec_time, memory = benchmark_algorithm(func, data)
            results.append({
                "Dataset": name,
                "Algorithm": algo_name,
                "Execution Time (ms)": round(exec_time, 3),
                "Memory Usage (KB)": round(memory, 2)
            })
            print(f"{algo_name} on {name} data -> Time: {exec_time:.3f} ms | Memory: {memory:.2f} KB")

    # Store results in DataFrame
    df = pd.DataFrame(results)
    print("\n=== Performance Summary ===")
    print(df.to_string(index=False))

    # Save results to CSV for report/graph use
    df.to_csv("sorting_benchmark_results.csv", index=False)
    print("\nResults saved to 'sorting_benchmark_results.csv'")

if __name__ == "__main__":
    main()
