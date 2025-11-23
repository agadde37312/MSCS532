from src.linked_list import LinkedList

def test_linked_list_insert_delete():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)

    assert ll.search(20) is True
    ll.delete(20)
    assert ll.search(20) is False
