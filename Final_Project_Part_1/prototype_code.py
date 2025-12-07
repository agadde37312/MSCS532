import time
import numpy as np

# Naive Python list approach
size = 1000000
py_list = list(range(size))

start = time.time()
total = 0
for x in py_list:
    total += x * 2
end = time.time()
print("Python list time:", end - start)

# Optimized NumPy approach
np_array = np.arange(size)

start = time.time()
total_np = np_array * 2
end = time.time()
print("NumPy array time:", end - start)
