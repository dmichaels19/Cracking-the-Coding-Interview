class BinaryTree:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """
        In order traversal
        :return:
        """
        print(self.data, end='')
        if self.left != None:
            self.left.__str__()
        if self.right != None:
            self.right.__str__()

    def is_leaf(self):
        return True if (self.left == None and self.right == None) else False

def size(bin_tree):
    if bin_tree == None:
        return 0
    else:
        return sum(size(bin_tree.left), size(bin_tree.right)) + 1

def max_depth(bin_tree):
    if bin_tree == None:
        return 0
    elif bin_tree.is_leaf():
        return 1
    else:
        return max(max_depth(bin_tree.left), max_depth(bin_tree.right))

def to_list(self):
    if self != None:
        return [self.data, to_list(self.left), to_list(self.right)]
    else:
        return None

def has_path_sum(tree, target):
    def tree_sum(tr):
        if tr == None: return 0

        found, curr_sum = tree_sum(tr.left) + tree_sum(tr.right) + tr.data

        if curr_sum == 100 or found:
            return True, 100
        else:
            return False, curr_sum

    found, _ = tree_sum(tree)

def mirror(bin_tree):
    if bin_tree != None:
        mirrored_left = mirror(bin_tree.left)
        bin_tree.left = mirror(bin_tree.right)
        bin_tree.right = mirrored_left

def same_tree(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True
    elif not (tree1 == None or tree2 == None):
        return False
    else:
        return same_tree(tree1.left, tree2.left) and same_tree(tree1.left, tree2.right)

def countTrees(num_elems):
    if num_elems == 1:
        return 1
    else:
        return 2 * countTrees(num_elems - 1)
