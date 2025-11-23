from src.queue import Queue
import pytest

def test_queue_enqueue_dequeue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10
    assert q.dequeue() == 20

def test_queue_underflow():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
