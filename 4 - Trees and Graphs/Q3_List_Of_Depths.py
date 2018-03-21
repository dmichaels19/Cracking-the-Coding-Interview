"""
Chapter 4, Question 3
Given a binary tree, design an algorithm which creates a list (array or linked list) of
all the nodes at each depth (e.g., if you have a tree with depth D, you’ll have D lists).
"""

class BinaryTreeNode():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def list_of_depths(tree):
    DepthsList = []

    find_depths(tree, 0, DepthsList)

def find_depths(tree, height, DepthsList):
    # When we go beyond the leaves
    if tree is None:
        return

    # In the case that we haven't visited this height yet, create a list that will hold 
    #   elements at this height
    if len(DepthsList) <= height:
        DepthsList.append(list())
    
    DepthsList[height].append(tree.value)
    
    # Do a depth-first traversal on the left and right side
    recurse(tree.left, height + 1, DepthsList)
    recurse(tree.right, height + 1, DepthsList)



