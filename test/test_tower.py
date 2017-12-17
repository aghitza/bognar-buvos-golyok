import pytest
from src.cube import CubeTower, Cube

class TestTower(object):

    def test_tower_create(self):
        oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
        c1 = Cube(oplst)
        oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
        c2 = Cube(oplst)
        oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
        c3 = Cube(oplst)
        oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
        c4 = Cube(oplst)
        tower = CubeTower([c1, c2, c3, c4])
        assert True

    def test_tower_display(self):
        oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
        c1 = Cube(oplst)
        oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
        c2 = Cube(oplst)
        oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
        c3 = Cube(oplst)
        oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
        c4 = Cube(oplst)
        tower = CubeTower([c1, c2, c3, c4])
        disp1 = ' Y\nRBGG\n Y' 
        disp2 = ' G\nBRYY\n B' 
        disp3 = ' B\nRRYR\n G' 
        disp4 = ' G\nYRBB\n R' 
        display = disp1 + '\n\n' + disp2 + '\n\n' + disp3 + '\n\n' + disp4
        assert tower.display() == display

    def test_tower_configlst_self(self):
        oplst = [['Y', 'Y'], ['B', 'G'], ['R', 'G']]
        c0 = Cube(oplst)
        oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
        c1 = Cube(oplst)
        oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
        c2 = Cube(oplst)
        oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
        c3 = Cube(oplst)
        tower = CubeTower([c0, c1, c2, c3])
        assert tower in tower.configlst()

    def test_tower_configlst(self):
        oplst = [['Y', 'Y'], ['B', 'G'], ['R', 'G']]
        c0 = Cube(oplst)
        oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
        c1 = Cube(oplst)
        oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
        c2 = Cube(oplst)
        oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
        c3 = Cube(oplst)
        tower = CubeTower([c0, c1, c2, c3])
        c = c0.views()[1]
        tower2 = CubeTower([c, c1, c2, c3])
        assert tower2 in tower.configlst()
