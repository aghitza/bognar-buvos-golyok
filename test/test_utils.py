"""
Test auxiliary functions.
"""
from src.cube import _cyclic_permutations

def test_cyclic_permutations_empty():
    """Cyclic permutations of the empty list"""
    lst = []
    assert _cyclic_permutations(lst) == [[]]

def test_cyclic_permutations_one():
    """Cyclic permutations of a singleton list"""
    lst = [1]
    assert _cyclic_permutations(lst) == [[1]]

def test_cyclic_permutations_two():
    """Cyclic permutations of a two-element list"""
    lst = [1, 2]
    assert _cyclic_permutations(lst) == [[1, 2], [2, 1]]

def test_cyclic_permutations_larger():
    """Cyclic permutations of a larger list"""
    lst = [1, 2, 3, 4, 5, 6]
    res = [[1, 2, 3, 4, 5, 6],
           [2, 3, 4, 5, 6, 1],
           [3, 4, 5, 6, 1, 2],
           [4, 5, 6, 1, 2, 3],
           [5, 6, 1, 2, 3, 4],
           [6, 1, 2, 3, 4, 5]]
    assert _cyclic_permutations(lst) == res
