from collections import defaultdict

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

#class BinaryTree():
#    def __init__(self, val):
#        self.value = val
#        self.left  = None
#        self.right = None

def find_num_sums(target, root):
    def find_num_sums_helper(curr_node, prev_sums, running_sum):
        if curr_node is None:
            print("Root found")
            return 0

        sub_count = 0

        running_sum += curr_node.value
        prev_sums[running_sum] += 1

        if (running_sum - target) in prev_sums:
            sub_count += prev_sums[running_sum - target]
        elif target == running_sum:
            sub_count += 1

        print(sub_count)

        sub_count += find_num_sums_helper(curr_node.left, prev_sums, running_sum)
        sub_count += find_num_sums_helper(curr_node.right, prev_sums, running_sum)
        
        if prev_sums[running_sum] == 1:
            del prev_sums[running_sum]
        else:
            prev_sums[running_sum] -= 1

        return sub_count

    return find_num_sums_helper(root, defaultdict(int), 0)


left = Node(None,None,3)
right = Node(None,None,3)
root = Node(left,right,3)
root.left.left = Node(None,None,3)
root.left.right = Node(None,None,3)
root.right.left = Node(None,None,3)
root.right.right = Node(None,None,3)

print(find_num_sums(6, root))
