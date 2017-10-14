def search(arr, target, rotated = False):
    def bin_search(min_index, max_index):
        mid_index = min_index + int((max_index - min_index) / 2)

        if min_index > max_index:
            return -1

        if arr[mid_index] > target:
            return bin_search(min_index, mid_index-1)
        elif arr[mid_index] < target:
            return bin_search(mid_index+1, max_index)
        else:
            return mid_index


    def find_pivot(min_index, max_index):
        if min_index > max_index:
            return -1
        if min_index == max_index:
            return min_index

        while (min_index < max_index):
            mid_index = min_index + int((max_index - min_index) / 2)

            if arr[min_index] > arr[mid_index]:
                max_index = mid_index - 1


    return bin_search_rotated(0, len(arr)-1, False)

#
# for i in range(100):
#     assert search(list(range(100)), i) == i
# for i in range(101):
#     assert search(list(range(101)), i) == i
# assert search(list(range(101)), -1) == -1
# assert search(list(range(101)), 7.5) == -1

for i in range(100)[49:50]:
    arr = list(range(100))
    arr = arr[i:] + arr[:i]
    for j in range(100)[49:50]:
        print(j, arr)
        search(arr, j)
