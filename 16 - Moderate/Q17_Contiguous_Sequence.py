
def find_contiguous_sequence(sequence):
    max_sum = 0
    max_start = max_end = 0
    curr_start = curr_end = 0
    curr_sum = 0

    while curr_end < len(sequence):
        curr_sum += sequence[curr_end]
        while curr_sum < 0 and curr_start <= curr_end:
            curr_sum -= sequence[curr_start]
            curr_start += 1
        if curr_sum > max_sum:
            max_start = curr_start
            max_end = curr_end
            max_sum = curr_sum
        curr_end += 1
    while curr_start < len(sequence):
        curr_sum -= sequence[curr_start]
        curr_start += 1
        if curr_sum > max_sum:
            max_start = curr_start
            max_end = curr_end
            max_sum = curr_sum
            
    # In the case where all numbers are negative
    if max_sum == max_start == max_end == 0:
        max_sum = -float('inf')
        for i, val in enumerate(sequence):
            if val > max_sum:
                max_sum = val
                max_start = max_end = i
    return (max_sum, max_start, max_end)

print(find_contiguous_sequence([-8,-3,-2,-4,-10]))
