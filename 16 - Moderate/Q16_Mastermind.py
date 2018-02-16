color_map = {
        'R' : 0,
        'G' : 1, 
        'Y' : 2,
        'B' : 3
        }
def color_to_tuple(color_str):
    """
    color_str: String of length 4 where each character is either 
                'R', 'G', 'Y', or 'B'.
    return: Tuple of length 4 of ints in range 0-3.
    """
    
    if not len(color_str) == 4:
        raise Error("Color input should be of length 4, not {}".format(len(color_str)))

    color_str = color_str.upper()
    output_list = []
    for val in color_str:
        if val in color_map:
            output_list.append(color_map[val])
        else:
            raise Error("Unknown color given: {}".format(val))
    return tuple(output_list)

def get_guess_metrics(guess, solution):
    guess_parsed = color_to_tuple(guess)
    solution_parsed = color_to_tuple(solution)

    hits = 0
    for i in range(4):
        if guess_parsed[i] == solution_parsed[i]:
            hits += 1
            # Flag each hit as used 
            guess_parsed[i] = -1
            solution_parsed[i] = -1
    
    pseudo_hits = 0
    for i in guess_parsed:
        if not i == -1:
            for j in range(4):
                if solution_parsed[j] == i:
                    pseudo_hits += 1
                    # Flag each hit as used
                    solution_parsed[j] = -1

    return (hits, pseudo_hits)

