class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def insert(node, key):
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    # LL Case
    if balance > 1 and key < node.left.key:
        print(f"LL Rotation at node {node.key}")
        return right_rotate(node)

    # RR Case
    if balance < -1 and key > node.right.key:
        print(f"RR Rotation at node {node.key}")
        return left_rotate(node)

    # LR Case
    if balance > 1 and key > node.left.key:
        print(f"LR Rotation at node {node.key}")
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # RL Case
    if balance < -1 and key < node.right.key:
        print(f"RL Rotation at node {node.key}")
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

N = int(input())
values = list(map(int, input().split()))

root = None
for val in values:
    root = insert(root, val)
