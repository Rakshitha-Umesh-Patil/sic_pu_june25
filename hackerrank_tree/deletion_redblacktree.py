from collections import deque

class Node:
    def __init__(self, key, color):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, 'B') 
        self.root = self.NIL

    def level_order_build(self, keys, colors):
        n = len(keys)
        if n == 0:
            return

        nodes = [Node(keys[i], colors[i]) for i in range(n)]
        for node in nodes:
            node.left = node.right = self.NIL

        self.root = nodes[0]
        queue = deque()
        queue.append(self.root)
        index = 1

        for node in nodes:
            if index < n:
                node.left = nodes[index]
                nodes[index].parent = node
                index += 1
            if index < n:
                node.right = nodes[index]
                nodes[index].parent = node
                index += 1
            if index >= n:
                break

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, key):
        z = self.search(self.root, key)
        if z == self.NIL:
            return  # Key not found

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'B':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == 'B' and w.right.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.right.color == 'B':
                        w.left.color = 'B'
                        w.color = 'R'
                        self.rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.right.color = 'B'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if w.left.color == 'B' and w.right.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.left.color == 'B':
                        w.right.color = 'B'
                        w.color = 'R'
                        self.rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.left.color = 'B'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'B'

    def search(self, node, key):
        if node == self.NIL or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

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

    def level_order_print(self):
        result_keys = []
        result_colors = []
        queue = deque()
        if self.root == self.NIL:
            return result_keys, result_colors

        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if node == self.NIL:
                continue
            result_keys.append(node.key)
            result_colors.append(node.color)
            queue.append(node.left)
            queue.append(node.right)
        return result_keys, result_colors

n = int(input())
keys = list(map(int, input().split()))
colors = input().split()
delete_key = int(input())

rbt = RedBlackTree()
rbt.level_order_build(keys, colors)
rbt.delete(delete_key)

keys_out, colors_out = rbt.level_order_print()
print(*keys_out)
print(*colors_out)
