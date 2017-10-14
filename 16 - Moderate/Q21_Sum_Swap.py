def list_swap(A, B):
    """

    :param A: first list
    :param B: second list
    :return: Tuple of two elements, None if not possible
    """

    diff = sum(A) - sum(B)
    if diff % 2 != 0:
        return None

    set_B = set(B)

    for a in A:
        b = a - int(diff / 2)
        if b in set_B:
            return (a, b)

    return None

if __name__ == "__main__":
    print(list_swap([1,0,4,7], [2,6,10]))