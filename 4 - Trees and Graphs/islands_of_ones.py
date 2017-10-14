def findIslands(arr, n, m):

    def set_island_to_zero(arr, init_i, init_j):
        arr[init_i][init_j] = 0
        # Each tuple in the list corresponds to a valid position for a
        # new one in the same island
        for (add_i, add_j) in [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i!= 0 and j != 0]:
            new_i = init_i + add_i
            new_j = init_j + add_j
            correct_j = new_j < m and new_j >= 0
            correct_i = new_i < n and new_i >= 0
            if correct_i and correct_j and arr[new_i][new_j] == 1:
                set_island_to_zero(arr, init_i + add_i, init_j + add_j)

    total_islands = 0
    for i in range(len(arr)):

        for j, bool in enumerate(arr[i]):
            if bool:
                set_island_to_zero(arr, i, j)
                total_islands += 1
    return total_islands
