# benchmarks.py
import random
import time
import csv
from copy import deepcopy
from randomized_quicksort import randomized_quicksort, deterministic_quicksort
from hash_table_chaining import HashTableChaining

def generate_random(n):
    return [random.randint(0, n*10) for _ in range(n)]

def generate_sorted(n):
    return list(range(n))

def generate_reverse(n):
    return list(range(n, 0, -1))

def generate_repeated(n, k=5):
    # only k distinct values
    vals = [random.randint(0, 1000) for _ in range(k)]
    return [random.choice(vals) for _ in range(n)]

def time_sort(func, arr, trials=3):
    total = 0.0
    for _ in range(trials):
        a = list(arr)
        t0 = time.perf_counter()
        func(a)
        t1 = time.perf_counter()
        total += (t1 - t0)
    return total / trials

def test_quicksorts(sizes=(1000, 5000, 10000), trials=3):
    kinds = [
        ("random", generate_random),
        ("sorted", generate_sorted),
        ("reverse", generate_reverse),
        ("repeated", generate_repeated),
    ]
    rows = []
    for n in sizes:
        for name, gen in kinds:
            arr = gen(n)
            rtime = time_sort(lambda a: randomized_quicksort(a, 0, len(a)-1) if len(a)>0 else None, arr, trials=trials)
            dtime = time_sort(lambda a: deterministic_quicksort(a, 0, len(a)-1) if len(a)>0 else None, arr, trials=trials)
            rows.append((n, name, rtime, dtime))
            print(f"n={n} type={name} randomized={rtime:.6f}s deterministic={dtime:.6f}s")
    # write CSV
    with open("quicksort_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "type", "randomized_time", "deterministic_time"])
        writer.writerows(rows)

def test_hash_table(n=100000):
    ht = HashTableChaining(initial_capacity=16)
    keys = [f"key{i}" for i in range(n)]
    random.shuffle(keys)
    t0 = time.perf_counter()
    for i, k in enumerate(keys):
        ht.insert(k, i)
    t1 = time.perf_counter()
    insert_time = t1 - t0
    # search sample
    sample = random.sample(keys, min(1000, n))
    t0 = time.perf_counter()
    for k in sample:
        _ = ht.search(k)
    t1 = time.perf_counter()
    search_time = (t1 - t0) / len(sample)
    # delete sample
    t0 = time.perf_counter()
    for k in sample:
        ht.delete(k)
    t1 = time.perf_counter()
    delete_time = (t1 - t0) / len(sample)
    print(f"Inserted {n} items in {insert_time:.4f}s; avg search time {search_time*1e6:.2f}µs; avg delete time {delete_time*1e6:.2f}µs")
    with open("hashtable_results.txt", "w") as f:
        f.write(f"Inserted {n} items in {insert_time:.4f}s\navg search time {search_time*1e6:.2f}µs\navg delete time {delete_time*1e6:.2f}µs\n")

if __name__ == "__main__":
    # adjust sizes if running on limited hardware
    test_quicksorts(sizes=(1000, 5000, 10000), trials=3)
    test_hash_table(n=50000)
