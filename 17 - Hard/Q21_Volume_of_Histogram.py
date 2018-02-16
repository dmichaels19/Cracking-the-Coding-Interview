def create_reverse_max_array(array):
    reverse_max_array = [0 for x in range(len(array))]
    curr_max = 0
    for i in range(len(array) -1 ,-1, -1):
        if array[i] > curr_max:
            curr_max = array[i]
        reverse_max_array[i] = curr_max
    return reverse_max_array


def find_total_water_volume(array, reverse_max_array):
    i = 0
    curr_peak = array[i]
    total_volume = 0

    while i < len(array) - 1:
        i += 1
        if array[i] > curr_peak:
            curr_peak = array[i]
        else:
            total_volume += min(curr_peak, reverse_max_array[i]) - array[i]
    return total_volume

def volume_of_histogram(hist):
    reverse_max_array = create_reverse_max_array(hist)
    print(reverse_max_array)
    return find_total_water_volume(hist, reverse_max_array)

print(volume_of_histogram([10,0,4,0,0,6,0,0,3,0,5,0,1,0,0,0]))


