from astar import astarzenji


def main():

    # zenjifield [N,O,S,W]
    # values:   0 = block
    #           1 = entry
    #           2 = exit
    #           3 = source (water input, no rotation)
    #           4 = goal (water outlet, no rotation)
    zenjifield = [[[3, 2, 2, 3], [2, 0, 1, 0], [1, 2, 2, 1], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 1, 2], [0, 1, 2, 2], [0, 0, 2, 1]],
                  [[0, 0, 2, 1], [1, 0, 2, 0], [1, 2, 1, 2], [0, 1, 0, 2]],
                  [[1, 2, 0, 0], [1, 2, 0, 1], [1, 2, 0, 0], [1, 4, 4, 1]]]

    # row, column
    zenjistart = (0, 0)
    zenjiend = (3, 3)

    # calculate a*
    path = astarzenji(zenjifield, zenjistart, zenjiend)

    # map and path output
    print("********************************************************************************")
    print("** Zenji start                                                                **")
    print("********************************************************************************")
    print()
    print("Zenji, field:")
    for line in zenjifield:
        print(line)
    print()
    print("Zenji, path to goal ( position ( x, y ), rotation ):")
    if path is None:
        print("ERROR NO PATH FOUND ;(")
    else:
        for node in path:
            print(node)
    print()
    print("********************************************************************************")
    print("** Zenji end                                                                  **")
    print("********************************************************************************")
    print()


if __name__ == '__main__':
    main()
