# hash_table_chaining.py
import math
import random

class HashTableChaining:
    def __init__(self, initial_capacity=8, max_load_factor=0.75):
        self.capacity = max(8, initial_capacity)
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        self.max_load_factor = max_load_factor
        # random odd multiplier for simple multiplicative hashing
        self._mult = random.randrange(1, 2**31 - 1, 2)  

    def _hash(self, key):
        # convert key to integer via builtin hash, then multiplicative method
        h = hash(key)
        # 64-bit mixing then multiplicative
        x = (h ^ (h >> 16)) & 0xFFFFFFFFFFFFFFFF
        # multiplication by odd constant then shift
        m = (x * self._mult) & 0xFFFFFFFFFFFFFFFF
        # map to bucket index
        return (m >> (64 - int(math.log2(self.capacity)))) % self.capacity

    def _resize(self, new_capacity):
        old_items = []
        for bucket in self.buckets:
            for k, v in bucket:
                old_items.append((k, v))
        self.capacity = max(8, new_capacity)
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for k, v in old_items:
            self.insert(k, v)

    def _ensure_capacity(self):
        if self.size / self.capacity > self.max_load_factor:
            self._resize(self.capacity * 2)

    def insert(self, key, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        self._ensure_capacity()

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def __len__(self):
        return self.size
