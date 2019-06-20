from astar import astarzenji


def main():

    print()
    print("********************************************************************************")
    print("** Zenji A* start                                                             **")
    print("********************************************************************************")
    print()

    # zenjifield [N,O,S,W]
    # values:   0 = block
    #           1 = entry
    #           2 = exit
    #           3 = source
    #           4 = goal
    zenjifield = [[[2, 2, 2, 2], [2, 0, 1, 0], [1, 2, 2, 1], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 1, 2], [0, 1, 2, 2], [0, 0, 2, 1]],
                  [[0, 0, 2, 1], [1, 0, 2, 0], [1, 2, 1, 2], [0, 1, 0, 2]],
                  [[1, 2, 0, 0], [1, 2, 0, 1], [1, 2, 0, 0], [1, 1, 1, 1]]]

    # x, y, rot
    zenjistart = (0, 0)
    zenjiend = (3, 3)
    print()
    print("Zenji, field:")
    for line in zenjifield:
        print(line)
    print()

    path = astarzenji(zenjifield, zenjistart, zenjiend)
    print()
    print("Zenji, path to goal ( position ( x, y ), rotation ):")
    if path is None:
        print("ERROR NO PATH FOUND ;(")
    else:
        for node in path:
            print(node)
    print()

    print("********************************************************************************")
    print("** Zenji A* end                                                               **")
    print("********************************************************************************")
    print()


if __name__ == '__main__':
    main()
