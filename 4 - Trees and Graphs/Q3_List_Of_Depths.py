class BinaryTreeNode():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def listOfDepths(tree):
    """

    :param tree:
    :return:
    """

    DepthsList = []

    recurse(tree, 0, DepthsList)

def recurse(tree, height, DepthsList):
    if tree is None:
        return

    if len(DepthsList) <= height:
        DepthsList.append([tree.value])
    else:
        DepthsList[height].append(tree.value)

    recurse(tree.left, height+1, DepthsList)
    recurse(tree.left, height + 1, DepthsList)



