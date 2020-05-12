class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = data

    def depth_first_max_sum(self, node, total, visit):
        # append total once leaf is reached
        if node.left is None and node.right is None:
            visit(total + node.data)
            return
        
        # traverse each node, adding data to sum until leaf
        for new_node in (node.left, node.right):
            if new_node is None:
                pass
            else:
                self.depth_first_max_sum(new_node, total + node.data, visit)

    
    def depth_first_superbalanced(self, node, total, visit):
        # append total once leaf is reached
        if node.left is None and node.right is None:
            visit(total + 1)
            return
        
        # traverse each node, adding data to sum until leaf
        for new_node in (node.left, node.right):
            if new_node is None:
                pass
            else:
                self.depth_first_superbalanced(new_node, total + 1, visit)


def max_sum(tree):
    """Given a binary tree containing numbers, find the maximum
    sum path (the path that has the largest sum of node values).
    """
    sums = []
    tree.depth_first_max_sum(tree.root, 0, sums.append)
    sums.sort(reverse=True)
    return sums[0]


def superbalanced(tree):
    """Let's say a binary tree is "superbalanced" if the difference
    between the depths of any two leaf nodes is at most one. Write
    a function to check if a binary tree is "superbalanced"."""
    depths = []
    tree.depth_first_superbalanced(tree.root, 0, depths.append)
    depths.sort(reverse=True)
    last_depth = None
    for depth in depths:
        if last_depth is None:
            pass
        elif last_depth - depth > 1:
            return False
        last_depth = depth
    return True






if __name__ == "__main__":
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(7)

    node8 = BinaryTreeNode(8)
    node9 = BinaryTreeNode(9)
    node7.right = node8
    node8.right = node9

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    tree = BinaryTree(node1)
    print('max sum is', max_sum(tree))
    print('tree is superbalanced:', superbalanced(tree))