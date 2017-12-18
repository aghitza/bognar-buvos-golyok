"""
Test the methods of the CubeTower object.
"""
from src.cube import CubeTower, Cube


def test_tower_create():
    """Check tower creation"""
    cubes = []
    oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
    cubes.append(Cube(oplst))
    oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
    cubes.append(Cube(oplst))
    _ = CubeTower(cubes)
    assert True

def test_tower_str():
    """Check tower printing"""
    cubes = []
    oplst = [['Y', 'Y'], ['R', 'G'], ['B', 'G']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
    cubes.append(Cube(oplst))
    oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
    cubes.append(Cube(oplst))
    tower = CubeTower(cubes)
    disp1 = ' Y\nRBGG\n Y'
    disp2 = ' G\nBRYY\n B'
    disp3 = ' B\nRRYR\n G'
    disp4 = ' G\nYRBB\n R'
    display = disp1 + '\n\n' + disp2 + '\n\n' + disp3 + '\n\n' + disp4
    assert str(tower) == display

def test_tower_configlst_self():
    """Check whether tower appears in its list of possible configurations"""
    cubes = []
    oplst = [['Y', 'Y'], ['B', 'G'], ['R', 'G']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
    cubes.append(Cube(oplst))
    oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
    cubes.append(Cube(oplst))
    tower = CubeTower(cubes)
    assert tower in tower.configlst()

def test_tower_configlst():
    """Check whether a simple permutation appears in configurations list"""
    cubes = []
    oplst = [['Y', 'Y'], ['B', 'G'], ['R', 'G']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
    cubes.append(Cube(oplst))
    oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
    cubes.append(Cube(oplst))
    tower = CubeTower(cubes)
    cube = cubes[0].views()[1]
    tower2 = CubeTower([cube] + cubes[1:])
    assert tower2 in tower.configlst()

def test_tower_not_winning():
    """Check a non-winning configuration"""
    cubes = []
    oplst = [['Y', 'Y'], ['B', 'G'], ['R', 'G']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'B'], ['B', 'Y'], ['R', 'Y']]
    cubes.append(Cube(oplst))
    oplst = [['B', 'G'], ['R', 'Y'], ['R', 'R']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'R'], ['Y', 'B'], ['R', 'B']]
    cubes.append(Cube(oplst))
    tower = CubeTower(cubes)
    assert tower.is_winning() is False

def test_tower_winning():
    """Check a winning configuration"""
    cubes = []
    oplst = [['Y', 'Y'], ['B', 'G'], ['R', 'G']]
    cubes.append(Cube(oplst))
    oplst = [['G', 'B'], ['Y', 'B'], ['Y', 'R']]
    cubes.append(Cube(oplst))
    oplst = [['R', 'R'], ['R', 'Y'], ['G', 'B']]
    cubes.append(Cube(oplst))
    oplst = [['B', 'R'], ['G', 'R'], ['B', 'Y']]
    cubes.append(Cube(oplst))
    tower = CubeTower(cubes)
    assert tower.is_winning() is True
