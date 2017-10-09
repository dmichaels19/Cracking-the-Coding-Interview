"""
You have an integer matrix representing a plot of land, where the value at that location
represents the height above sea level. A value of zero indicates water. A pond is a region
of water connected vertically, horizontally, or diagonally. The size of the pond is the
total number of connected water cells. Write a method to compute the sizes of all ponds
in the matrix.
"""


def pond_size(terrain, i, j):
    """

    :param terrain: the array of terrain heights
    :param i: the current row in the array
    :param j: the current column in the array
    :return: the size of the sub-problem pond size (ish)
    """

    # The size of the current pond
    size = 0
    if terrain[i][j] is 0:
        size = 1
    else:
        return size

        # Indicate that we have seen and already counted water in current block
        terrain[i][j] = -1

    arr = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]

    for tup in arr:
        row = (i + tup[0])
        col = (j + tup[1])
        if row >= 0 and row < len(terrain) and col >= 0 and col < len(terrain[i]):
            size += pond_size(terrain, row, col)

    return size


def find_ponds(terrain):
    """

    :param terrain: the array of terrain heights
    :return: Pond sizes
    """

    ponds = []
    for i, row in enumerate(terrain):
        for j, block in enumerate(row):
            if block == 0:
                ponds.append(pond_size(terrain, i, j))

    return ponds
