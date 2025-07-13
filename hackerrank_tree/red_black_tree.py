class Node:
    def __init__(self, data):
        self.data = data
        self.color = "R"  # New nodes are red by default
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = "B"
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if not parent:
            self.root = new_node
        elif data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "R"
        self.fix_insert(new_node)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k != self.root and k.parent.color == "R":
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right
                if uncle.color == "R":
                    k.parent.color = "B"
                    uncle.color = "B"
                    k.parent.parent.color = "R"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    self.rotate_right(k.parent.parent)
            else:
                uncle = k.parent.parent.left
                if uncle.color == "R":
                    k.parent.color = "B"
                    uncle.color = "B"
                    k.parent.parent.color = "R"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    self.rotate_left(k.parent.parent)
        self.root.color = "B"

    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            print(f"{node.data}({node.color})", end=" ")
            self.inorder(node.right)

n = int(input())
values = list(map(int, input().split()))

rbt = RedBlackTree()
for val in values:
    rbt.insert(val)

rbt.inorder(rbt.root)
