from src.stack import Stack
import pytest

def test_stack_push_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1

def test_stack_underflow():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
