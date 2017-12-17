import pytest
from src.cube import Cube

class TestCube(object):

    def test_cube_create(self):
        oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
        c = Cube(oplst)
        assert True

    def test_cube_oplst(self):
        oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
        c = Cube(oplst)
        assert c.oplst() == oplst

    def test_cube_display(self):
        oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
        c = Cube(oplst)
        disp = ' Y\nRBGG\n Y' 
        assert c.display() == disp

    def test_cube_views(self):
        oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
        c = Cube(oplst)
        displays = []
        displays.append(' Y\nRBGG\n Y')
        displays.append(' Y\nBGGR\n Y')
        displays.append(' Y\nGGRB\n Y')
        displays.append(' Y\nGRBG\n Y')
        displays.append(' R\nBYGY\n G')
        displays.append(' R\nYGYB\n G')
        displays.append(' R\nGYBY\n G')
        displays.append(' R\nYBYG\n G')
        displays.append(' B\nYRYG\n G')
        displays.append(' B\nRYGY\n G')
        displays.append(' B\nYGYR\n G')
        displays.append(' B\nGYRY\n G')
        views = sorted([x.display() for x in c.views()])
        assert views == sorted(displays)

