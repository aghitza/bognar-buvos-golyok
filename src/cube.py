class Cube(object):

    def __init__(self, oplst):
        self._opposites = oplst

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
