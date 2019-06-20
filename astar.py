from node import ZenjiNode


def checkhasexit(node=None, direction=None):
    print("check exit: " + str(node.blockrot[node.rotpos][direction]))
    if node.blockrot[node.rotpos][direction] == 2:
        return True
    else:
        return False


def checkhasentries(node, direction):
    entries = []
    count = 0
    childdir = 0
    if direction == 0:
        childdir = 2
    if direction == 1:
        childdir = 3
    if direction == 2:
        childdir = 0
    if direction == 3:
        childdir = 1
    for block in node.blockrot:
        print("check entry: " + str(block[childdir]))
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
    print("start A *")
    print()

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        print("load first in open list")
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            print("check for smaller f " + str(item.f) + " < " + str(current_node.f))
            if item.f < current_node.f:
                current_node = item
                current_index = index
                print("get better node from open list")

        print("workingnode: "+str(current_node.position)+","+str(current_node.rotpos))

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        print("added closed list")

        # Found the goal
        if current_node == end_node:
            print("found end")
            path = []
            current = current_node
            while current is not None:
                path.append((current.position, current.rotpos))
                current = current.parent
            print("created path")
            return path[::-1]
            # Return reversed path

        # Generate children
        print("generate children list")
        children = []
        direction = 0
        print("check adjacent squares")
        # Adjacent squares west north east south
        for new_position in [(0, -1), (1, 0), (0, 1), (-1, 0)]:

            # Get node position
            if new_position == (-1, 0):
                direction = 2
            elif new_position == (0, 1):
                direction = 1
            elif new_position == (0, -1):
                direction = 3
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(field) - 1) or node_position[0] < 0 or node_position[1] > (len(field[len(field)-1]) -1) or node_position[1] < 0:
                print("out of range")
                continue

            print("check exit")
            # check node has exit
            if checkhasexit(current_node, direction):
                print("create child")
                # Create new node
                new_node = ZenjiNode(current_node, node_position, field[node_position[0]][node_position[1]])

                # check child has entry
                entries = checkhasentries(new_node, direction)
                for entry in entries:
                    # Append
                    print("add child")
                    new_node.rotpos = entry
                    children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            print("current_node.g: " + str(current_node.g))
            print("current_node.rotpos: " + str(current_node.rotpos))
            print("child.rotpos: " + str(child.rotpos))
            child.g = current_node.g + 1 + current_node.rotpos + child.rotpos
            print("child.g: " + str(child.g))
            child.h = 2 * ((end_node.position[0] - child.position[0]) + (end_node.position[1] - child.position[1]))
            print("child.h: " + str(child.h))
            child.f = child.g + child.h
            print("child.f: " + str(child.f))

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
