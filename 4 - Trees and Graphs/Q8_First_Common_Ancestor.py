"""
Given a binary tree (not a binary search tree) and two values say n1 and n2,
write a program to find the least common ancestor.

"""

class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_common_ancestor(curr_node, n1, n2):
    """
    
    :param curr_node:
    :param n1:
    :param n2:
    :return: 3-tuple: whether subtree has n1 (Boolean), whether subtree has n2 (Boolean), 
                whether subtree has common ancestor (Boolean or the node itself if True). If so,
                return the value.
    """
    if curr_node is None:
        return False, False, False

    left_has_n1, left_has_n2, left_has_common_node = find_common_ancestor(curr_node.left, n1, n2)
    right_has_n1, right_has_n2, right_has_common_node = find_common_ancestor(curr_node.left, n1, n2)

    curr_has_n1 = curr_node.data == n1 
    curr_has_n2 = curr_node.data == n2 

    # Is true if left subtree, right subtree, or current node has the desired N
    return_n1 = left_has_n1 or right_has_n1 or curr_has_n1
    return_n2 = right_has_n2 or right_has_n2 or curr_has_n2

    # In the case that we are the common ancestor vs. if one of our subtrees has the common ancestor
    if (curr_has_n1 or curr_has_n2) and (return_n1 and return_n2):
        return_common = curr_node
    else:
        return_common = left_has_common_node or right_has_common_node

    return return_n1, return_n2, return_common
