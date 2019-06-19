from node import ZenjiNode


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

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append((current.position, current.rotpos))
                current = current.parent
            return path[::-1]
            # Return reversed path

        # ATWORK Generate children
        children = []
        if current_node.parent is None:
            for new_position in [(1, 0), (0, 1)]: # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(field) - 1) or node_position[0] < 0 or node_position[1] > (len(field[len(field)-1]) -1) or node_position[1] < 0:
                    continue

                # Create new node
                new_node = ZenjiNode(current_node, node_position, field[node_position[0]][node_position[1]])

                # Append
                children.append(new_node)
        else:
            for new_position in [(0, -1), (1, 0), (0, 1), (-1, 0)]: # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(field) - 1) or node_position[0] < 0 or node_position[1] > (len(field[len(field)-1]) -1) or node_position[1] < 0:
                    continue

                # Create new node
                new_node = ZenjiNode(current_node, node_position, field[node_position[0]][node_position[1]])

                # Append
                children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
