from collections import deque
import math

class BTreeNode:
    def __init__(self, t, is_leaf):
        self.t = t  # Minimum degree
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        if self.is_leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.is_leaf)

        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]

        if not y.is_leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.append(root)
            new_root.split_child(0)
            i = 0
            if key > new_root.keys[0]:
                i += 1
            new_root.children[i].insert_non_full(key)
            self.root = new_root
        else:
            root.insert_non_full(key)

    def level_order_traversal(self):
        result = []
        q = deque()
        q.append(self.root)

        while q:
            level_size = len(q)
            level_keys = []

            for _ in range(level_size):
                node = q.popleft()
                level_keys.extend(node.keys)
                for child in node.children:
                    q.append(child)

            print(' '.join(map(str, level_keys)))


# === Driver Code ===
n, m = map(int, input().split())
keys = list(map(int, input().split()))

t = math.ceil(m / 2)
btree = BTree(t)

for key in keys:
    btree.insert(key)

btree.level_order_traversal()
