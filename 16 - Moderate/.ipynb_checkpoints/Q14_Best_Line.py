problem = """
Given a two-dimensional graph with points on it, find a line which passes through the most number of points
"""

X = 0
Y = 1
SLOPE = 0
Y_INTERCEPT = 1


def find_line_between_two_points(p1, p2):
    # In the case that we have a vertical line with infinite slope
    denom = float(p2[X] - p1[X])
    if denom == 0:
        slope = float("inf")
        y_intercept = p1[Y]
    else:
        slope = float(p2[Y] - p1[Y]) / denom
        y_intercept = p1[Y] - slope * p1[X]
    return (slope, y_intercept)


def find_line(points_list):
    all_points_pairs = [(first, second) for i, first in enumerate(points_list)
                        for j, second in enumerate(points_list) if i != j]

    # The if statement takes care of the special case when we have two equal points (infinite lines through
    # the same point)
    lines = [find_line_between_two_points(x, y) for x, y in all_points_pairs if x != y]

    # Find the line that is most frequent within the lines generated between all possible points
    number_of_pairs_passing_through_line = {}
    max_number = 0
    line_with_max = None
    for line in lines:
        # print number_of_pairs_passing_through_line
        new = number_of_pairs_passing_through_line.get(line, 0) + 1
        number_of_pairs_passing_through_line[line] = new
        if new > max_number:
            max_number = new
            line_with_max = line
    return line_with_max


if __name__ == "__main__":
    line =  find_line([(0, 0), (1, 1), (0, 2)])
    print "Slope: ", line[SLOPE]
    print "Y-Intercept: ", line[Y_INTERCEPT]