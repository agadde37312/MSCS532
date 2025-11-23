import pytest
from src.array_structure import Array

def test_array_insert_delete():
    arr = Array()
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)
    assert arr.get(1) == 20

    arr.delete(1)
    assert arr.get(1) == 30

def test_array_out_of_bounds():
    arr = Array()
    arr.insert(5)
    with pytest.raises(IndexError):
        arr.get(10)
