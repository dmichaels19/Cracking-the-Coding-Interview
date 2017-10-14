import set

# Unit test: Test that the card_tuple_to_string and its inverse function are correct
all_cards = [(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3)]
for card in all_cards:
    assert card == set.card_string_to_tuple(set.card_tuple_to_string(card))
assert "blue @@@" == set.card_tuple_to_string(set.card_string_to_tuple("blue @@@"))

# Functional testing: Check that input is read correctly for sample file
card_tuples, deck_size = set._get_data_from_file('sample_input_2.txt')
assert len(card_tuples) == deck_size

# Test on example from sample_input_2.txt file
SETS = set.get_all_sets(card_tuples)
assert len(SETS) == 41
greatest_sub_SETS = set.find_largest_disjoint_set(SETS)
assert len(greatest_sub_SETS) == 8