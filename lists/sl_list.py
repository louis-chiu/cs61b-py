from typing import Self, TypeVar

_IntNode = TypeVar("_IntNode", bound="SLList._IntNode")


class SLList:
    """
     A class that can store integer elements in a list.

     Attributes
     ----------
     sentinel : _IntNode
         A reference to a sentinel node which points to the first node in the SLList.
     size_ : int
         The size of the SLList.
     """
    sentinel: _IntNode
    size_: int

    class _IntNode:
        item: int | None
        next_: Self | None

        def __init__(self, item: int | None = None, next_: Self | None = None) -> None:
            self.item = item
            self.next_ = next_

    def __init__(self, x: int | None = None) -> None:
        self.sentinel = self._IntNode(None, None)
        self.size_ = 0

        if x is not None:
            self.sentinel.next_ = self._IntNode(x, None)
            self.size_ += 1

    def add_first(self, x: int) -> None:
        """Add x to the first of the list."""
        self.sentinel.next_ = self._IntNode(x, self.sentinel.next_)
        self.size_ += 1

    def get_first(self) -> int:
        """Return the first of the list."""
        return self.sentinel.next_.item

    def add_last(self, x: int) -> None:
        """Add x to the last of the list."""
        pointer: _IntNode = self.sentinel.next_

        while pointer.next_ is not None:
            pointer = pointer.next_

        pointer.next_ = self._IntNode(x, None)
        self.size_ += 1

    def size(self) -> int:
        """Return the size of the list by using cache."""
        return self.size_

    def size_recursively(self) -> int:
        """Return the size of the list recursively."""
        if self.sentinel.next_ is None:
            return 0
        return self._calculate_size(self.sentinel.next_)

    @classmethod
    def _calculate_size(cls, node: _IntNode) -> int:
        """Calculate the size of the list starting from the given node recursively."""
        if node.next_ is None:
            return 1
        return 1 + cls._calculate_size(node.next_)

    def size_iteratively(self) -> int:
        """Return the size of the list iteratively."""
        if self.sentinel.next_ is None:
            return 0

        pointer: _IntNode = self.sentinel.next_
        counter: int = 0
        while pointer is not None:
            counter += 1
            pointer = pointer.next_

        return counter
