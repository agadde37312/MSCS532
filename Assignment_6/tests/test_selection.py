import random
import pytest
from src.deterministic_selection import deterministic_select
from src.randomized_selection import randomized_select

# ---------- Test Basic Correctness ----------
def test_small_arrays():
    arr = [3, 1, 4, 1, 5, 9]
    assert deterministic_select(arr[:], 0) == min(arr)
    assert deterministic_select(arr[:], 5) == max(arr)

    assert randomized_select(arr[:], 0) == min(arr)
    assert randomized_select(arr[:], 5) == max(arr)

# ---------- Test Duplicate Handling ----------
def test_duplicates():
    arr = [5, 5, 5, 5, 1, 1, 9]
    assert deterministic_select(arr[:], 0) == 1
    assert randomized_select(arr[:], 0) == 1

# ---------- Randomized Stress Test ----------
def test_randomized_correctness():
    for _ in range(50):
        arr = [random.randint(0, 1000) for _ in range(200)]
        k = random.randint(0, len(arr)-1)

        expected = sorted(arr)[k]

        assert deterministic_select(arr[:], k) == expected
        assert randomized_select(arr[:], k) == expected

# ---------- Adversarial Inputs ----------
def test_sorted_adversarial():
    arr = list(range(5000))
    assert deterministic_select(arr[:], 2500) == 2500
    assert randomized_select(arr[:], 2500) == 2500

def test_reverse_sorted_adversarial():
    arr = list(range(5000))[::-1]
    assert deterministic_select(arr[:], 1000) == 3999
