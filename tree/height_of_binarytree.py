class TreeNode:
    def __init__(self, x):
        self.x = x
        self.L = None
        self.R = None


def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data <= root.x:
        root.L = insert(root.L, data)
    else:
        root.R = insert(root.R, data)
    return root


def height(root):
    if root is None:
        return -1  
    return 1 + max(height(root.L), height(root.R))
print("enter: ")
n = int(input()) 
arr = list(map(int, input().split()))

root = None
for val in arr:
    root = insert(root, val)

print(height(root))
