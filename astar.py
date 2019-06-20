from node import ZenjiNode


# checks if a node has a exit in this direction
def checkhasexit(node=None, direction=None):
    # debug output
    print("node: " + str(node.blockrot))
    print("direction: " + str(direction))
    print("rotpos: " + str(node.rotpos))
    print("check exit: " + str(node.blockrot[node.rotpos][direction]) + " == 2")
    # 2 == exit
    if node.blockrot[node.rotpos][direction] == 2:
        return True
    else:
        return False


# checks if a node has an entry on our opposite direction
def checkhasentries(node, direction):
    entries = []
    count = 0

    # get opposite direction
    childdir = 0
    if direction == 0:
        childdir = 2
    if direction == 1:
        childdir = 3
    if direction == 2:
        childdir = 0
    if direction == 3:
        childdir = 1

    # check all rotations for entries
    for block in node.blockrot:
        # debug output
        print("check entry: " + str(block[childdir]))
        # 1 == entry
        if block[childdir] == 1:
            entries.append(count)
        count += 1
    return entries


def astarzenji(field, start, end):
    """Returns a list of tuples and a rotation as a path from the given start to the given end in the given field"""

    print("start: "+ str(field[start[0]][start[1]]))
    print("end: "+ str(field[end[0]][end[1]]))

    # Create start and end node
    start_node = ZenjiNode(None, start, field[start[0]][start[1]])
    start_node.g = start_node.h = start_node.f = 0
    end_node = ZenjiNode(None, end, field[end[0]][end[1]])
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    print()
    print("********************************************************************************")
    print("** Zenji A* calculation start                                                 **")
    print("********************************************************************************")
    print()

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        # debug output
        print("load first in open list")
        current_node = open_list[0]
        current_index = 0
        # Loop open list
        for index, item in enumerate(open_list):
            # debug output
            print("check for smaller f " + str(item.f) + " < " + str(current_node.f))
            if item.f < current_node.f:
                current_node = item
                current_index = index
                # debug output
                print("get better node from open list")

        # debug output
        print("workingnode: "+str(current_node.position)+","+str(current_node.rotpos))

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        # debug output
        print("added closed list")

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            # create the path
            while current is not None:
                path.append((current.position, current.rotpos))
                current = current.parent
            # debug output
            print("created path")
            print()
            print("********************************************************************************")
            print("** Zenji A* calculation end                                                   **")
            print("********************************************************************************")
            print()
            # Return reversed path
            return path[::-1]

        # Generate children
        # debug output
        print("generate children list")
        children = []
        # debug output
        print("check adjacent squares")
        # Adjacent squares n,e,s,w
        for direction in [0, 1, 2, 3]:

            # Get node position
            if direction == 0:
                node_position = (current_node.position[0]-1, current_node.position[1])
            elif direction == 1:
                node_position = (current_node.position[0], current_node.position[1]+1)
            elif direction == 2:
                node_position = (current_node.position[0]+1, current_node.position[1])
            elif direction == 3:
                node_position = (current_node.position[0], current_node.position[1]-1)
            # check range
            if node_position[0] < 0 or node_position[1] < 0 or node_position[0] >= len(field) or node_position[1] >= len(field[0]):
                # debug output
                print("out of range")
                continue

            # debug output
            print("check exit")
            # check node has exit
            if checkhasexit(current_node, direction):
                # debug output
                print("create child")
                # Create new node
                new_node = ZenjiNode(current_node, node_position, field[node_position[0]][node_position[1]])

                # check child has entry
                entries = checkhasentries(new_node, direction)
                for entry in entries:
                    # debug output
                    print("add child")
                    # Append
                    new_node.rotpos = entry
                    children.append(new_node)
                    new_node = ZenjiNode(current_node, node_position, field[node_position[0]][node_position[1]])

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1 + current_node.rotpos + child.rotpos
            child.h = 2 * ((end_node.position[0] - child.position[0]) + (end_node.position[1] - child.position[1]))
            child.f = child.g + child.h

            # debug output
            print("current_node.g: " + str(current_node.g))
            print("current_node.rotpos: " + str(current_node.rotpos))
            print("child.rotpos: " + str(child.rotpos))
            print("child.g: " + str(child.g))
            print("child.h: " + str(child.h))
            print("child.f: " + str(child.f))

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
