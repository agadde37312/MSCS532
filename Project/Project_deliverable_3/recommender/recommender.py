import numpy as np
from collections import defaultdict, deque
import heapq
import logging
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SparseMatrix:
    """Optimized sparse matrix for user-item interactions with batch insertion."""
    def __init__(self):
        self.data = defaultdict(dict)

    def insert(self, user, item, rating):
        self.data[user][item] = rating

    def insert_batch(self, interactions):
        for user, item, rating in interactions:
            self.insert(user, item, rating)

    def get_user_items(self, user):
        return self.data.get(user, {})

class MatrixFactorization:
    """Optimized matrix factorization with caching of scores."""
    def __init__(self, num_users, num_items, embedding_dim=32, seed=42, cache_scores=True):
        np.random.seed(seed)
        self.user_embeddings = np.random.rand(num_users, embedding_dim)
        self.item_embeddings = np.random.rand(num_items, embedding_dim)
        self.cache_scores = cache_scores
        if cache_scores:
            self._score_cache = {}

    def score(self, user_id, item_id):
        if self.cache_scores:
            key = (user_id, item_id)
            if key not in self._score_cache:
                self._score_cache[key] = np.dot(self.user_embeddings[user_id], self.item_embeddings[item_id])
            return self._score_cache[key]
        return np.dot(self.user_embeddings[user_id], self.item_embeddings[item_id])

class LSHIndex:
    """Optimized LSH for approximate nearest neighbors with incremental updates."""
    def __init__(self, embedding_dim=32, num_planes=16):
        self.hyperplanes = np.random.randn(num_planes, embedding_dim)
        self.buckets = defaultdict(set)

    def hash_vector(self, vector):
        bits = vector @ self.hyperplanes.T
        signature = ''.join(['1' if x > 0 else '0' for x in bits])
        return signature

    def insert(self, item_id, vector):
        sig = self.hash_vector(vector)
        self.buckets[sig].add(item_id)

    def insert_batch(self, items_vectors):
        for item_id, vector in items_vectors.items():
            self.insert(item_id, vector)

    def query(self, vector):
        sig = self.hash_vector(vector)
        return self.buckets.get(sig, set())

class Recommender:
    """Optimized hybrid recommender with heap-based top-k and optional multithreading."""
    def __init__(self, num_users=10, num_items=20, embedding_dim=32):
        self.sparse_matrix = SparseMatrix()
        self.mf = MatrixFactorization(num_users, num_items, embedding_dim)
        self.lsh = LSHIndex(embedding_dim)

        # Prepopulate LSH efficiently
        items_vectors = {i: self.mf.item_embeddings[i] for i in range(num_items)}
        self.lsh.insert_batch(items_vectors)

    def add_interaction(self, user, item, rating):
        if user < 0 or item < 0:
            logging.warning("Invalid user/item ID")
            return
        self.sparse_matrix.insert(user, item, rating)

    def add_interactions_batch(self, interactions):
        self.sparse_matrix.insert_batch(interactions)

    def get_top_k_recommendations(self, user_id, k=5, use_multithreading=False):
        if user_id not in self.sparse_matrix.data:
            logging.warning(f"User {user_id} not found, returning empty list")
            return []

        user_vec = self.mf.user_embeddings[user_id]
        candidates = self.lsh.query(user_vec)
        scores = []

        def compute_score(item):
            return (item, self.mf.score(user_id, item))

        if use_multithreading:
            with ThreadPoolExecutor() as executor:
                scores = list(executor.map(compute_score, candidates))
        else:
            scores = [compute_score(item) for item in candidates]

        # Use heap for O(n log k) top-k selection
        top_k = heapq.nlargest(k, scores, key=lambda x: x[1])
        return top_k

if __name__ == "__main__":
    rec = Recommender(num_users=50, num_items=100, embedding_dim=32)
    # Batch add sample interactions
    interactions = [(i % 50, i % 100, np.random.randint(1, 6)) for i in range(200)]
    rec.add_interactions_batch(interactions)

    top_k = rec.get_top_k_recommendations(0, k=5, use_multithreading=True)
    print("Top-5 recommendations for user 0:", top_k)
