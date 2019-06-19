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

    def getblock(self):
        return self.blockrot[self.rotpos]

    def setrotpos(self, newpos):
        self.rotpos = newpos

    def getrotpos(self,):
        return self.rotpos

    def __eq__(self, other):
        return self.position == other.position


class Node:
    """A zenjinode class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
