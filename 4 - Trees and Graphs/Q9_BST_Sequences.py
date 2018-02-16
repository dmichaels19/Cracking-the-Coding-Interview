"""
A binary search tree was created by traversing throug han array from left to right and inserting each element. give a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
"""

from collections import deque
import itertools

class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return not (self.left or self.right)

def find_BST_sequences(root):
    def find_sequences_helper(curr_node):
        if curr_node is None:
            return []
        if curr_node.isLeaf():
            return [[curr_node.value]]
        possible_sequences_left = find_sequences_helper(curr_node.left)
        possible_sequences_right = find_sequences_helper(curr_node.right)

        new_sequences = []
        curr_value = [curr_node.value]

        if not (possible_sequences_left and possible_sequences_right):
            return [curr_value + seq for seq in itertools.chain(possible_sequences_left, possible_sequences_right)]
        
        for seq_left in possible_sequences_left:
            for seq_right in possible_sequences_right:
                new_sequences.append(curr_value + seq_left + seq_right)
                new_sequences.append(curr_value + seq_right + seq_left)

        return new_sequences

    return find_sequences_helper(root)

root = BinaryTree(5)
root.left = BinaryTree(3)
#root.left.right = BinaryTree(4)
#root.left.left = BinaryTree(2)
root.right = BinaryTree(7)
#root.right.left = BinaryTree(6)
#root.right.right = BinaryTree(8)

print(find_BST_sequences(root))

