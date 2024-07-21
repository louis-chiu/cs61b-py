from algorithms.sort import Sort


class TestSort:
    """Test the sort functionality."""

    def test_selection_sort(self):
        input_ = ['i', 'have', 'an', 'egg', 'egg']
        expected = ['an', 'egg', 'egg', 'have',  'i']
        Sort.selection_sort(input_)
        assert input_ == expected

        input_ = [1, 2, 3, 5, 1235, 3, -10, 5]
        expected = [-10, 1, 2, 3, 3, 5, 5, 1235]
        Sort.selection_sort(input_)
        assert input_ == expected

        input_ = [3.1, 4.1, 2.5, 3.6, 0.1, 2.0, 5.5]
        expected = [0.1, 2.0, 2.5, 3.1, 3.6, 4.1, 5.5]
        Sort.selection_sort(input_)
        assert input_ == expected

    def test_find_smallest_index(self):
        input_ = [1, 2, 3, 5, 1235, -10]
        expected = -10
        assert input_[Sort.find_index_of_smallest(input_)] == expected

        input_ = ['i', 'have', 'an', 'egg']
        expected = 'an'
        assert input_[Sort.find_index_of_smallest(input_)] == expected

    def test_swap(self):
        input_ = [1, 2, 3, 5, 1235, -10]
        expect = [1, 2, 5, 3, 1235, -10]
        Sort.swap(input_, 2, 3)
        assert input_ == expect

        input_ = ['i', 'have', 'an', 'egg']
        expected = ['egg', 'have', 'an', 'i']
        Sort.swap(input_, 0, 3)
        assert input_ == expected




