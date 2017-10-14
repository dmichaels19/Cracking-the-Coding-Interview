def unsort(deck):
    """
    sorts an unsorted deck of cards with numbers 1-13 and suits S, D, C, and H

    :param deck: a list of cards where each card is of the form "##A" where ## is the card's number and A is its suit
    :return: sorted deck
    """
    suits = {'S' : [], 'D' : [], 'C' : [], 'H' : []}
    for card in deck:
        # Appends card to its proper suit
        suits[card[-1]].append(card)
