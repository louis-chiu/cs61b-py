from typing import Self, TypeVar

_Node = TypeVar("_Node", bound="DLList._Node")
T = TypeVar('T')


class DLList[T]:
    """
     A class that can store elements of type T in a doubly linked list.
     This implementation uses two sentinel nodes.

     Attributes
     ----------
     sentinel_front : _IntNode
         A reference to a sentinel node whose next_ attribute points to the first node in the DLList.
     sentinel_back : _IntNode
         A reference to a sentinel node whose prev attribute points to the last node in the DLList
     size_ : int
         The size of the DLList.
     """
    sentinel_front: _Node
    sentinel_back: _Node
    size_: int

    class _Node:
        prev: Self | None
        item: T | None
        next_: Self | None

        def __init__(self, item: T | None = None, prev: Self | None = None, next_: Self | None = None) -> None:
            self.prev = prev
            self.item = item
            self.next_ = next_

    def __init__(self, x: T | None = None) -> None:
        self.sentinel_front = self._Node(None, None, None)
        self.sentinel_back = self._Node(None, None, None)
        self.size_ = 0

        if x is not None:
            new_node = self._Node(x, None, None)
            self.sentinel_front.next_ = new_node
            self.sentinel_back.prev = new_node
            self.size_ += 1

    def add_first(self, x: T) -> None:
        """Add x to the first of the list."""
        self.sentinel_front.next_ = self._Node(x, None, self.sentinel_front.next_)
        self.size_ += 1

    def get_first(self) -> T:
        """Return the first element of the list."""
        return self.sentinel_front.next_.item

    def add_last(self, x: T) -> None:
        """Add x to the last of the list."""
        self.sentinel_back.prev = self._Node(x, self.sentinel_back.prev, None)
        self.size_ += 1

    def get_last(self) -> T:
        """Return the last element of the list."""
        return self.sentinel_back.prev.item

    def remove_last(self) -> None:
        """Remove the last element of the list."""
        if self.size_ == 0:
            raise IndexError("The list is empty.")
        elif self.size_ == 1:
            self.sentinel_back.prev = None
            self.sentinel_front.next_ = None
        else:
            self.sentinel_back.prev = self.sentinel_back.prev.prev
        self.size_ -= 1

    def size(self) -> int:
        """Return the size of the list by using cache."""
        return self.size_

