import pytest
from src.cube import _cyclic_permutations

class TestUtils(object):

    def test_cyclic_permutations_empty(self):
        lst = []
        assert _cyclic_permutations(lst) == [[]]

    def test_cyclic_permutations_singleton(self):
        lst = [1]
        assert _cyclic_permutations(lst) == [[1]]

    def test_cyclic_permutations_pair(self):
        lst = [1, 2]
        assert _cyclic_permutations(lst) == [[1, 2], [2, 1]]

    def test_cyclic_permutations_pair(self):
        lst = [1, 2, 3, 4, 5, 6]
        res = [[1, 2, 3, 4, 5, 6],
               [2, 3, 4, 5, 6, 1],
               [3, 4, 5, 6, 1, 2],
               [4, 5, 6, 1, 2, 3],
               [5, 6, 1, 2, 3, 4],
               [6, 1, 2, 3, 4, 5]]
        assert _cyclic_permutations(lst) == res
