from astar import astar, astarzenji


def main():

    print()

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print("Maze Example, path to goal:")
    print(path)
    print()
    print()
    print("********************************************************************************")
    print("** Zenji")
    print("********************************************************************************")
    print()

    # zenjifield [N,O,S,W]
    # values:   0 = block
    #           1 = entry
    #           2 = exit
    #           3 = source
    #           4 = goal
    zenjifield = [[[3, 3, 2, 2], [2, 0, 1, 0], [1, 2, 2, 1], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 1, 2], [0, 1, 2, 2], [0, 0, 2, 1]],
                  [[0, 0, 2, 1], [1, 0, 2, 0], [1, 2, 1, 2], [0, 1, 0, 2]],
                  [[1, 2, 0, 0], [1, 2, 0, 1], [1, 2, 0, 0], [1, 4, 4, 1]]]

    # x, y, rot
    zenjistart = (0, 0)
    zenjiend = (3, 3)

    path = astarzenji(zenjifield, zenjistart, zenjiend)
    print("Zenji, path to goal:")
    print(path)


if __name__ == '__main__':
    main()
