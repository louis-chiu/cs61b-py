from typing import TypeVar
import numpy as np
from numpy.typing import NDArray

T = TypeVar("T", bound=np.generic, covariant=True)


class AList[T]:
    """
     A class that can store elements of type U in a array list.
     """
    items: NDArray[T]
    size_: int
    _RESIZE_FACTOR: int = 2

    def __init__(self) -> None:
        self.items = np.empty(100, dtype=object)
        self.size_ = 0

    def add_last(self, item: T) -> None:
        """Add an item to the end of the list."""
        if self.size_ >= self.items.size * 0.25:
            self._resize(self.items.size * self._RESIZE_FACTOR)

        self.items[self.size_] = item
        self.size_ += 1

    def get_last(self) -> T:
        """Get the last item from the list."""
        return self.items[self.size_ - 1]

    def get(self, i: int) -> T:
        """Get item at index i from the list."""
        return self.items[i]

    def remove_last(self) -> None:
        if self.items.size * 0.25 > self.size_:
            self._resize(self.items.size // self._RESIZE_FACTOR)
        self.items[self.size_ - 1] = None
        self.size_ -= 1

    def _resize(self, capacity: int) -> None:
        new_array = np.empty(capacity, dtype=object)
        new_array[:self.size_] = self.items[:self.size_]
        self.items = new_array

    def size(self) -> int:
        """Return the size of the list."""
        return self.size_
