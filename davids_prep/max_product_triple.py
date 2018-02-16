"""
A unsorted array of integers is given;
you need to find the max product formed my multiplying three numbers.
"""

def max_product(l):
    """
    Of three numbers, either exactly two or zero numbers can be negative to get a positive result.

    :param l: list of elements
    :return:
    """
    min_two_negatives = [0,0]
    max_three_positives = [0,0,0]

    for next_val in l:
        max_of_mins = max(min_two_negatives)
        if next_val < max_of_mins:
            index = min_two_negatives.index(max_of_mins)
            min_two_negatives[index] = next_val

        min_of_maxs = min(max_three_positives)
        if next_val > min_of_maxs:
            index = max_three_positives.index(min_of_maxs)
            max_three_positives[index] = next_val

    min_product = min_two_negatives[0] * min_two_negatives[1]
    max_three_positives = sorted(max_three_positives)
    max_product_first_two = max_three_positives[0] * max_three_positives[1]
    product_of_first_two = max(max_product_first_two, min_product)

    return product_of_first_two * max_three_positives[2]


print(max_product(list([-10,-1, 9,8,7, 10])))

