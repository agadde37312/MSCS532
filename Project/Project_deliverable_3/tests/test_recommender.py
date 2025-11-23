import pytest
import numpy as np
from recommender.recommender import Recommender

# -----------------------------
# Fixtures
# -----------------------------
@pytest.fixture
def small_recommender():
    """Create a small recommender with 10 users and 20 items."""
    return Recommender(num_users=10, num_items=20, embedding_dim=16)

@pytest.fixture
def large_recommender():
    """Create a larger recommender for stress testing."""
    return Recommender(num_users=100, num_items=500, embedding_dim=32)


# -----------------------------
# Test Cases
# -----------------------------

def test_sparse_matrix_insertion(small_recommender):
    """Test inserting and retrieving user-item interactions."""
    rec = small_recommender
    rec.add_interaction(0, 1, 5)
    rec.add_interaction(0, 2, 3)
    user_items = rec.sparse_matrix.get_user_items(0)
    assert user_items[1] == 5
    assert user_items[2] == 3
    assert isinstance(user_items, dict)


def test_top_k_recommendations_non_empty(small_recommender):
    """Ensure top-k recommendations return correct number of items."""
    rec = small_recommender
    # Add interactions
    for item in range(5):
        rec.add_interaction(0, item, np.random.randint(1, 6))
    top_k = rec.get_top_k_recommendations(0, k=3)
    assert len(top_k) == 3
    # Each entry should be a tuple (item_id, score)
    assert all(isinstance(t, tuple) and len(t) == 2 for t in top_k)


def test_top_k_empty_user(small_recommender):
    """Check that recommendations handle users with no interactions."""
    rec = small_recommender
    top_k = rec.get_top_k_recommendations(5, k=3)
    # Should still return a list (possibly empty if LSH misses)
    assert isinstance(top_k, list)
    assert len(top_k) <= 3


def test_ann_retrieval_accuracy(small_recommender):
    """Test that ANN returns some candidate items."""
    rec = small_recommender
    user_vec = rec.mf.user_embeddings[0]
    candidates = rec.lsh.query(user_vec)
    # Should return a list of item IDs
