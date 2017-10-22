"""
Given two (singly) linked lists, determine if the lists intersect. Return the intersecting node.
"""

class LL_Node():
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

    def __len__(self):
        temp = self
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count


def get_intersection(ll_node_1, ll_node_2):
    len_1 = len(ll_node_1)
    len_2 = len(ll_node_2)
    diff = abs(len_2 - len_1)

    if len_1 == 0 or len_2 == 0:
        return None

    nth_node = ll_node_1
    for _ in range(diff-1):
        nth_node = nth_node.next
    
    return nth_node
