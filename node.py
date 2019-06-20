class ZenjiNode:
    """A node class for A* Pathfinding for zenji problem"""

    def __init__(self, parent=None, position=None, blockrot=None):
        # set parent node
        self.parent = parent
        # set node position (row, column)
        self.position = position

        # create all block rotations from initial block
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

        # set zero rotation
        self.rotpos = 0

        # set zero a* values
        self.g = 0
        self.h = 0
        self.f = 0

        # debug output
        print("rotpos 0: " + str(self.blockrot[0]))
        print("rotpos 1: " + str(self.blockrot[1]))
        print("rotpos 2: " + str(self.blockrot[2]))
        print("rotpos 3: " + str(self.blockrot[3]))

    def __eq__(self, other):
        # equal means same position and rotation
        return self.position == other.position and self.rotpos == other.rotpos
