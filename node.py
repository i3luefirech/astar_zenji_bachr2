class ZenjiNode:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, blockrot=None):
        self.parent = parent
        self.position = position

        if self.parent is None:
            self.blockrot = [[blockrot[0], blockrot[1], blockrot[2], blockrot[3]],
                             [blockrot[0], blockrot[1], blockrot[2], blockrot[3]],
                             [blockrot[0], blockrot[1], blockrot[2], blockrot[3]],
                             [blockrot[0], blockrot[1], blockrot[2], blockrot[3]]]
        else:
            self.blockrot = [[blockrot[0], blockrot[1], blockrot[2], blockrot[3]],
                             [blockrot[3], blockrot[0], blockrot[1], blockrot[2]],
                             [blockrot[2], blockrot[3], blockrot[0], blockrot[1]],
                             [blockrot[1], blockrot[2], blockrot[3], blockrot[0]]]
        self.rotpos = 0
        self.inuse = 0

        self.g = 0
        self.h = 0
        self.f = 0

        print("rotpos 0: " + str(self.blockrot[0]))
        print("rotpos 1: " + str(self.blockrot[1]))
        print("rotpos 2: " + str(self.blockrot[2]))
        print("rotpos 3: " + str(self.blockrot[3]))

    def getblock(self):
        return self.blockrot[self.rotpos]

    def setrotpos(self, newpos):
        self.rotpos = newpos

    def getrotpos(self,):
        return self.rotpos

    def __eq__(self, other):
        return self.position == other.position and self.rotpos == other.rotpos
