"""
Please use Python 2.7. Call with:
$ your_input_text.txt | python set.py
"""

import sys

# Conversion mappings from attribute to value.
# The index of each attribute is its value
COLORS = ['blue', 'green', 'yellow']
SYMBOLS = ['aA@', 'sS$', 'hH#']
SHADINGS = ['ash','ASH', '@$#']

# Indices for the value of each attribute in card_tuple
COL = 0
NUM = 1
SYM = 2
SHADE = 3

def _get_value_from_mapping(key, mapping):
    """
    Gives a numerical value to each sub-type (key) of card types. Common pattern for value lookup.

    :param key: substring to search for in mapping
    :param mapping:
    :return: index of key location in mapping
    """
    for i, lookup in enumerate(mapping):
        if key in lookup:
            return i

def card_string_to_tuple(card_string):
    """
    Of the form: (Color, Number, Symbol, Shade).

    :param card_string:
    :return: 4-tuple representation of card type
    """
    color_str, other_attributes_str = card_string.split(" ")
    char = other_attributes_str[0]

    color = _get_value_from_mapping(color_str, COLORS)
    number = len(other_attributes_str) - 1
    symbol = _get_value_from_mapping(char, SYMBOLS)
    shading = _get_value_from_mapping(char, SHADINGS)
    
    card_tuple = (color, number, symbol, shading)
    return card_tuple 

def card_tuple_to_string(card_tuple):
    """
    Convert back from card_tuple to string.

    """
    color = COLORS[card_tuple[COL]]

    # Get the shading group ('ash','ASH', '@$#').
    # Then get the appropriate symbol from the shading group. Note that the ith index is all the same symbol
    shading_subset = SHADINGS[card_tuple[SHADE]]
    symbol_with_shading = shading_subset[card_tuple[SYM]]
    repeated = symbol_with_shading * (card_tuple[NUM] + 1)

    return color + " " + repeated

def _get_data_from_file(file='sample_input.txt'):
    """
    For debugging and testing purposes. Load input from file

    """
    with open(file, 'r') as f:
        data = f.read()
        data = data.split("\n")
    deck_size = int(data[0])
    card_tuples = map(lambda x: card_string_to_tuple(x), data[1:])

    return card_tuples, deck_size

def _get_data_from_stdin():
    """
    Pre-process data from standard input and convert card strings to tuples
    :return: tuple of (card_tuples, deck_size)
    """
    data = sys.stdin.readlines()
    cleaned_data = map(lambda x: x.strip("\n"), data)

    deck_size = int(cleaned_data[0])
    card_tuples = map(lambda x: card_string_to_tuple(x), cleaned_data[1:])
    return card_tuples, deck_size

def _is_SET(card1, card2, card3):
    """
    Checks if 3 cards form a set.
    :return: Boolean
    """
    for i in range(4):
        # All cards are unique --> unique_vals = 3, All cards are the same --> unique_vals = 1
        unique_vals = len(set([card1[i], card2[i], card3[i]]))
        if unique_vals == 2:
            return False
    return True



def get_all_sets(card_tuples):
    """
    From a set of cards, finds all sets in O(N^3) time by trying every combination (N choose K total combinations)

    """
    SETS = []
    deck_size = len(card_tuples)

    # TODO: Make more pythonic
    for card1, i in zip(card_tuples, range(deck_size)):
        for card2, j in zip(card_tuples[i+1:], range(i+1, deck_size)):
            for card3, k in zip(card_tuples[j+1:], range(j+1, deck_size)):
                if _is_SET(card1, card2, card3):
                    SETS.append((card1, card2, card3))
    return SETS

def find_largest_disjoint_set(SETS):
    """
    Uses derivation of Depth First Search (of a binary tree) to find largest disjoint set.
    Visits the current set of cards (node) and sees if it can add it to the current set of disjoint sets.
        If it can, it will explore the next card (node) assuming that the current set of cards is part of the new
         disjoint set.
        Once that subtree is explored, the current set of cards card is removed from the disjoint set.
    Then, it explores the next set of cards card without itself added to the disjoint set.

    You can think of the left child of a set of cards as the disjoint set where the current set of cards is included and
     the right child of a set of cards as the disjoint set where the current set of cards is not included. The only
      time the left subtree is explored is if the current set of cards can be added to the disjoint set.

    :param SETS:
    :return: set of SETs (tuple).
    """
    union = set()   # The current union of disjoint sets
    sub_SETS = set()    # The current set of disjoint sets
    greatest_sub_SETS = set()
    
    # Where all the recursion is done
    def try_adding_another_set(current_card_index):

        if current_card_index >= len(SETS):
            return
        current_card = SETS[current_card_index]

        is_valid_addition_to_union = True
        for s in current_card:
            if s in union:
                is_valid_addition_to_union = False

        if is_valid_addition_to_union:
            sub_SETS.add(current_card)
            union.update(current_card)
            if len(sub_SETS) > len(greatest_sub_SETS):
                greatest_sub_SETS.clear()
                greatest_sub_SETS.update(sub_SETS)

            # Explore the left subtree (where the current_card is included
            try_adding_another_set(current_card_index + 1)
            for s in current_card:
                union.remove(s)
            sub_SETS.remove(current_card)

        try_adding_another_set(current_card_index + 1)

    # The initial recursive call
    try_adding_another_set(0)
    return greatest_sub_SETS

if __name__ == "__main__":
    card_tuples, deck_size = _get_data_from_stdin()
    SETS = get_all_sets(card_tuples)
    greatest_sub_SETS = find_largest_disjoint_set(SETS)

    print len(SETS)
    print len(greatest_sub_SETS)
    for set in greatest_sub_SETS:
        print
        for card in set:
            print card_tuple_to_string(card)