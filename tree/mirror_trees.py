class TreeNode:
    def __init__(self, val):
        self.val = val
        self.L = None
        self.R = None

def are_mirrors(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (
        a.val == b.val and
        are_mirrors(a.L, b.R) and
        are_mirrors(a.R, b.L)
    )

def build_tree(n):
    nodes = {}
    for _ in range(n - 1):
        u, v, d = input().split()
        u, v = int(u), int(v)
        if u not in nodes:
            nodes[u] = TreeNode(u)
        if v not in nodes:
            nodes[v] = TreeNode(v)
        if d == 'L':
            nodes[u].L = nodes[v]
        else:
            nodes[u].R = nodes[v]
    return nodes[int(list(nodes.keys())[0])]  # Return root node

# Main
n = int(input())
root1 = build_tree(n)
root2 = build_tree(n)

print("yes" if are_mirrors(root1, root2) else "no")
