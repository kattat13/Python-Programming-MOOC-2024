
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child: 'Node' = None, right_child: 'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(root: Node):
    # Initialize the greatest value with the value of the current node
    greatest = root.value
 
    # Base case: If the node has no children, return its value
    if root.left_child is None and root.right_child is None:
        return root.value

    # If the node has a left child, find the greatest value in the left subtree
    if root.left_child is not None:
        left_max = greatest_node(root.left_child)
        # Update the greatest value if a greater value is found in the left subtree
        greatest = max(greatest, left_max)
        
    # If the node has a right child, find the greatest value in the right subtree
    if root.right_child is not None:
        right_max = greatest_node(root.right_child)
        # Update the greatest value if a greater value is found in the right subtree
        greatest = max(greatest, right_max)
    
    return greatest


if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))