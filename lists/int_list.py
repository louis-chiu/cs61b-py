from typing import Self


class IntList:
    first: int
    rest: Self | None

    def __init__(self, first: int, rest: Self | None) -> None:
        self.first = first
        self.rest = rest

    def iterative_size(self) -> int:
        """Iteratively get the size of the IntList"""
        if self.rest is None:
            return 1

        count: int = 0
        pointer: Self = self
        while pointer is not None:
            count += 1
            pointer = pointer.rest
        return count

    def size(self) -> int:
        """Recursively get the size of the IntList."""
        if self.rest is None:
            return 1

        return 1 + self.rest.size()

    def get(self, index: int) -> Self:
        """Get the value at index of the IntList."""
        if index >= self.size() or index < 0:
            raise IndexError("Out of range")

        count: int = 0
        pointer: Self = self
        while count != index:
            count += 1
            pointer = pointer.rest

        return pointer