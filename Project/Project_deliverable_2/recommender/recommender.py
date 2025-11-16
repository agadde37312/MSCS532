### **recommender/recommender.py**

import numpy as np
from collections import defaultdict

class SparseMatrix:
    """Sparse matrix for user-item interactions."""
    def __init__(self):
        self.data = defaultdict(dict)

    def insert(self, user, item, rating):
        self.data[user][item] = rating

    def get_user_items(self, user):
        return self.data.get(user, {})

class MatrixFactorization:
    """Simple matrix factorization to get embeddings."""
    def __init__(self, num_users, num_items, embedding_dim=32, seed=42):
        np.random.seed(seed)
        self.user_embeddings = np.random.rand(num_users, embedding_dim)
        self.item_embeddings = np.random.rand(num_items, embedding_dim)

    def score(self, user_id, item_id):
        return np.dot(self.user_embeddings[user_id], self.item_embeddings[item_id])

class LSHIndex:
    """Simple LSH for approximate nearest neighbors."""
    def __init__(self, embedding_dim=32, num_planes=10):
        self.hyperplanes = np.random.randn(num_planes, embedding_dim)
        self.buckets = defaultdict(list)

    def hash_vector(self, vector):
        bits = vector @ self.hyperplanes.T
        signature = ''.join(['1' if x > 0 else '0' for x in bits])
        return signature

    def insert(self, item_id, vector):
        sig = self.hash_vector(vector)
        self.buckets[sig].append(item_id)

    def query(self, vector):
        sig = self.hash_vector(vector)
        return self.buckets.get(sig, [])

class Recommender:
    """Main recommender system PoC."""
    def __init__(self, num_users=10, num_items=20, embedding_dim=32):
        self.sparse_matrix = SparseMatrix()
        self.mf = MatrixFactorization(num_users, num_items, embedding_dim)
        self.lsh = LSHIndex(embedding_dim)

        # Prepopulate LSH
        for item_id in range(num_items):
            self.lsh.insert(item_id, self.mf.item_embeddings[item_id])

    def add_interaction(self, user, item, rating):
        self.sparse_matrix.insert(user, item, rating)

    def get_top_k_recommendations(self, user_id, k=5):
        user_vec = self.mf.user_embeddings[user_id]
        candidates = self.lsh.query(user_vec)
        scores = [(item, self.mf.score(user_id, item)) for item in candidates]
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:k]

if __name__ == "__main__":
    rec = Recommender()
    # Add sample interactions
    rec.add_interaction(0, 1, 5)
    rec.add_interaction(0, 2, 4)
    top_k = rec.get_top_k_recommendations(0, k=3)
    print("Top-3 recommendations for user :", top_k)
