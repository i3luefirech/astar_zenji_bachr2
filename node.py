class ZenjiNode:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, blockrot=None):
        self.parent = parent
        self.position = position
        self.blockrot = [[blockrot[0], blockrot[1], blockrot[2], blockrot[3]],
                         [blockrot[3], blockrot[0], blockrot[1], blockrot[2]],
                         [blockrot[2], blockrot[3], blockrot[0], blockrot[1]],
                         [blockrot[1], blockrot[2], blockrot[3], blockrot[0]]]

        self.g = 0
        self.h = 0
        self.f = 0

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
