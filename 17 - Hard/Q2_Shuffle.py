from random import randint

def switch(deck, i, j):
    temp = deck[i]
    deck[i] = deck[j]
    deck[j] = temp

def shuffle_recurse(deck):
    """
    It's a little weird since everything is in place thanks to Python's
            pass by object reference. However, we will return the `deck`
            anyways.
    """
    def shuffle_help(deck, i):
        if i >= len(deck) - 1:
            return
        j = randint(i, len(deck) - 1)
        switch(deck, i, j)
        shuffle_help(deck, i+1)

    if len(deck) <= 1:
        return deck
    shuffle_help(deck, 0)
    return deck

def shuffle_iteratively(deck):
    if len(deck) <= 1:
        return deck
    for i in range(len(deck)):
        j = randint(i, len(deck) - 1)
        switch(deck, i, j)
    return deck

print(shuffle_recurse(list(range(52))))
print(shuffle_iteratively(list(range(52))))

