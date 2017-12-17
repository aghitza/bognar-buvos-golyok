class CubeTower(object):

    def __init__(self, cubelst):
        self._cubes = cubelst

    def cubelst(self):
        return self._cubes

    def display(self):
        cubelst = self.cubelst()
        return '\n\n'.join([c.display() for c in cubelst])

    def configlst(self):
        cubelst = self.cubelst()
        cfglst = []
        for c0 in cubelst[0].views():
            for c1 in cubelst[1].views():
                for c2 in cubelst[2].views():
                    for c3 in cubelst[3].views():
                        tower = CubeTower([c0, c1, c2, c3])
                        cfglst.append(tower)
        return cfglst

    def __eq__(self, other):
        return self.cubelst() == other.cubelst()


class Cube(object):

    def __init__(self, oplst):
        self._opposites = oplst

    def __eq__(self, other):
        return self.oplst() == other.oplst()

    def oplst(self):
        return self._opposites

    def display(self):
        oplst = self.oplst()
        disp = ' ' + oplst[0][0] + '\n'
        disp = disp + oplst[1][0] + oplst[2][0]
        disp = disp + oplst[1][1] + oplst[2][1]
        disp = disp + '\n' + ' ' + oplst[0][1]
        return disp

    def views(self):
        oplst = self.oplst()
        vlst = []
        for lst in _cyclic_permutations(oplst):
            vlst.append(Cube(lst))
            vlst.append(Cube([lst[0], lst[2], _reverse(lst[1])]))
            vlst.append(Cube([lst[0], _reverse(lst[1]), _reverse(lst[2])]))
            vlst.append(Cube([lst[0], _reverse(lst[2]), lst[1]]))
        #TODO? implement __cmp__ for Cube objects, and return sorted(vlst)
        return vlst


def _reverse(lst):
    nlst = lst.copy()
    nlst.reverse()
    return nlst


def _cyclic_permutations(lst):
    if lst == []:
        return [[]]
    plst = []
    for _ in range(len(lst)):
        plst.append(lst)
        lst = lst[1:] + [lst[0]]
    return plst
