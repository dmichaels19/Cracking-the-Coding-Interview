def majority_element(xs):
    """
    xs: input list. 
    return: Value from input list if Majority Element is found.
            Otherwise, -1
    """
    start = 0
    curr_index = 0
    count = 0

    while start < len(xs) / 2:

        curr_number = xs[start]
        count += 1
        curr_index = start + 1

        while count > 0:
            if xs[curr_index] == curr_number:
                count += 1
            else:
                count -= 1
            
            if curr_index < len(xs) -1:
                curr_index += 1
            else:
                curr_index = 0

            if curr_index == start:
                return curr_number

        while curr_number == xs[start]:
            start += 1
    return -1


print(majority_element([1,5,5,5,4,3,4]))
