"""
Code modeling the puzzle Bognar Buvos Golyok
(Hungarian version of Instant Insanity).
"""

class CubeTower(object):
    """Object for a tower of cubes"""

    def __init__(self, cubelst):
        self._cubes = cubelst

    def cubelst(self):
        """Return the list of cubes in the tower"""
        return self._cubes

    def __str__(self):
        """Print the tower configuration"""
        cubelst = self.cubelst()
        return '\n\n'.join([str(c) for c in cubelst])

    def __repr__(self):
        return str(self)

    def configlst(self):
        """Generate the list of all possible configurations of a tower"""
        return [CubeTower(t) for t in self.configcubelst()]

    def configcubelst(self):
        """Auxiliary method for generating the list of configurations"""
        cubelst = self.cubelst()
        if not cubelst:
            return []
        elif len(cubelst) == 1:
            return [[v] for v in cubelst[0].views()]
        cfglst = []
        for cube in cubelst[0].views():
            tower1 = CubeTower(cubelst[1:])
            clst1 = tower1.configcubelst()
            for cl1 in clst1:
                cblst = [cube] + cl1
                cfglst.append(cblst)
        return cfglst

    def __eq__(self, other):
        return self.cubelst() == other.cubelst()

    def is_winning(self):
        """
        Determine whether a configuration is winning, that is if every
        column of cube faces contains all distinct colors.
        """
        cubelst = self.cubelst()
        rows = [_flatten(c.oplst()[1:]) for c in cubelst]
        for j in range(4):
            column = [r[j] for r in rows]
            if len(set(column)) < len(column):
                return False
        return True


class Cube(object):
    """Object for one cube"""

    def __init__(self, oplst):
        self._opposites = oplst

    def __eq__(self, other):
        return self.oplst() == other.oplst()

    def __ge__(self, other):
        return self.oplst() >= other.oplst()

    def __gt__(self, other):
        return self.oplst() > other.oplst()

    def oplst(self):
        """Return the list of opposite faces of the cube"""
        return self._opposites

    def __str__(self):
        """String representation of the cube"""
        oplst = self.oplst()
        disp = ' ' + oplst[0][0] + '\n'
        disp = disp + oplst[1][0] + oplst[2][0]
        disp = disp + oplst[1][1] + oplst[2][1]
        disp = disp + '\n' + ' ' + oplst[0][1]
        return disp

    def __repr__(self):
        return str(self)

    def views(self):
        """Return all the possible views of the cube (with repetitions)"""
        oplst = self.oplst()
        vlst = []
        for lst in _cyclic_permutations(oplst):
            vlst.append(Cube(lst))
            vlst.append(Cube([_reverse(lst[0]), _reverse(lst[2]), _reverse(lst[1])]))
            vlst.append(Cube([lst[0], lst[2], _reverse(lst[1])]))
            vlst.append(Cube([_reverse(lst[0]), lst[1], _reverse(lst[2])]))
            vlst.append(Cube([lst[0], _reverse(lst[1]), _reverse(lst[2])]))
            vlst.append(Cube([_reverse(lst[0]), lst[2], lst[1]]))
            vlst.append(Cube([lst[0], _reverse(lst[2]), lst[1]]))
            vlst.append(Cube([_reverse(lst[0]), _reverse(lst[1]), lst[2]]))
        return sorted(vlst)


def _reverse(lst):
    """Return the reverse of lst without mutating lst"""
    nlst = lst.copy()
    nlst.reverse()
    return nlst


def _cyclic_permutations(lst):
    """Return the list of cyclic permutations of the list lst"""
    if lst == []:
        return [[]]
    plst = []
    for _ in range(len(lst)):
        plst.append(lst)
        lst = lst[1:] + [lst[0]]
    return plst


def _flatten(lst):
    """Flatten the list lst"""
    flst = [x for s in lst for x in s]
    return flst
