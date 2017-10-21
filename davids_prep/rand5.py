from random import randint
from collections import Counter



def get_rand5_from_7():
    """
    Generates a random number generator from a 7-sided die.
    1. Create a unique (random) number between 1 and 35 by rolling 7-sided die 5 times.
    2. Return random35 mod 5
    :return:
    """
    sum = 0
    for i in range(5):
        sum += randint(1, 7)  + 7 * i
    return sum % 5

