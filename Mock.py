class Node:
    def __init__(self):
        self.left = None
        self.right = None
def count(node):
    if not node:
        return 0
    count = 1
    def search(node, counter):
        if (node.left and node.right):
            return search(node.left, counter + 1) + search(node.right, counter + 1)
        elif (node.left):
            return search(node.left, 2 * counter)
        elif (node.right):
            return search(node.right,2 * counter + 1)
        return counter
    return search(node, count)

node = Node()
assert count(node) == 1, f'was expecting 1 but got {count(node)}'
assert count(None) == 0

node.right = Node()
node.right.right = Node()
assert count(node) == 3
node.right = None

node.left = Node()
node.left.left = Node()
assert count(node) == 3

# left and right