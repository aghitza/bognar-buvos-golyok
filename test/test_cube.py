"""
Test methods of the Cube object.
"""
from src.cube import Cube

def test_cube_create():
    """Test Cube object creation"""
    oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
    _ = Cube(oplst)
    assert True

def test_cube_oplst():
    """Test opposite pairs method"""
    oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
    cube = Cube(oplst)
    assert cube.oplst() == oplst

def test_cube_str():
    """Test string representation of Cube"""
    oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
    cube = Cube(oplst)
    strcube = ' Y\nRBGG\n Y'
    assert str(cube) == strcube

def test_cube_views():
    """Test the generation of all possible views of a cube"""
    oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
    cube = Cube(oplst)
    displays = []
    displays.append(' Y\nRBGG\n Y')
    displays.append(' Y\nGGBR\n Y')
    displays.append(' Y\nBGGR\n Y')
    displays.append(' Y\nRGGB\n Y')
    displays.append(' Y\nGGRB\n Y')
    displays.append(' Y\nBRGG\n Y')
    displays.append(' Y\nGRBG\n Y')
    displays.append(' Y\nGBRG\n Y')
    displays.append(' R\nBYGY\n G')
    displays.append(' G\nYGYB\n R')
    displays.append(' R\nYGYB\n G')
    displays.append(' G\nBYGY\n R')
    displays.append(' R\nGYBY\n G')
    displays.append(' G\nYBYG\n R')
    displays.append(' R\nYBYG\n G')
    displays.append(' G\nGYBY\n R')
    displays.append(' B\nYRYG\n G')
    displays.append(' G\nGYRY\n B')
    displays.append(' B\nRYGY\n G')
    displays.append(' G\nYGYR\n B')
    displays.append(' B\nYGYR\n G')
    displays.append(' G\nRYGY\n B')
    displays.append(' B\nGYRY\n G')
    displays.append(' G\nYRYG\n B')
    views = sorted([str(x) for x in cube.views()])
    assert views == sorted(displays)
