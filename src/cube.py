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
