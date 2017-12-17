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
