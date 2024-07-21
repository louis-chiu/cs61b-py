from typing import TypeVar

T = TypeVar('T')


class Sort:
    @classmethod
    def selection_sort(cls, lst: list[T]) -> None:
        """Apply the selection sort."""
        cls._selection_sort(lst, 0)

    @classmethod
    def _selection_sort(cls, lst: list[T], start_index: int) -> None:
        """A helper function to sort the list in ascending order."""
        if len(lst) == start_index:
            return
        index_of_smallest = cls.find_index_of_smallest(lst, start_index)
        cls.swap(lst, start_index, index_of_smallest)
        cls._selection_sort(lst, start_index + 1)

    @classmethod
    def find_index_of_smallest(cls, lst: list[T], start_index: int) -> int:
        """Find the index of the smallest value in the list."""
        if len(lst) - 1 == start_index:
            return start_index
        index_of_smallest: int = start_index
        tmp: T = lst[index_of_smallest]

        for (index, element) in enumerate(lst[start_index:]):
            if element <= tmp:
                tmp = element
                index_of_smallest = index
        return index_of_smallest + start_index

    @classmethod
    def swap(cls, lst: list[T], index: int, index_of_smallest: int) -> None:
        """Swap two elements in the list."""
        lst[index], lst[index_of_smallest] = lst[index_of_smallest], lst[index]
