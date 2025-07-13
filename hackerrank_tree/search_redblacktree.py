class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search(root, key):
    if not root:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Input
n = int(input())
nodes = {}
children = set()

# Build nodes
for _ in range(n):
    val, left, right = map(int, input().split())
    if val not in nodes:
        nodes[val] = Node(val)
    node = nodes[val]

    if left != -1:
        if left not in nodes:
            nodes[left] = Node(left)
        node.left = nodes[left]
        children.add(left)

    if right != -1:
        if right not in nodes:
            nodes[right] = Node(right)
        node.right = nodes[right]
        children.add(right)

root = None
for val in nodes:
    if val not in children:
        root = nodes[val]
        break

K = int(input())
print("Found" if search(root, K) else "Not Found")
