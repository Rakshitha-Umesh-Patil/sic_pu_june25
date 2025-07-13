from collections import deque
import math

class BTreeNode:
    def __init__(self, t, is_leaf):
        self.t = t
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.is_leaf:
            self.keys.append(0)
            while i >= 0 and key < self.keys[i]:
                self.keys[i+1] = self.keys[i]
                i -= 1
            self.keys[i+1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2*self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.is_leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t-1]
        if not y.is_leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        self.children.insert(i+1, z)
        self.keys.insert(i, y.keys.pop())

class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t

    def insert(self, key):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(key)
        else:
            if len(self.root.keys) == 2*self.t - 1:
                s = BTreeNode(self.t, False)
                s.children.append(self.root)
                s.split_child(0)
                i = 0
                if key > s.keys[0]:
                    i += 1
                s.children[i].insert_non_full(key)
                self.root = s
            else:
                self.root.insert_non_full(key)

    def delete(self, key):
        if not self.root:
            return
        self.root = self._delete(self.root, key)
        if self.root and len(self.root.keys) == 0:
            self.root = self.root.children[0] if self.root.children else None

    def _delete(self, node, key):
        if key in node.keys:
            idx = node.keys.index(key)
            if node.is_leaf:
                node.keys.pop(idx)
            else:
                pred = self._get_predecessor(node.children[idx])
                node.keys[idx] = pred
                node.children[idx] = self._delete(node.children[idx], pred)
        else:
            if node.is_leaf:
                return node  # Key not found
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            node.children[i] = self._delete(node.children[i], key)
        return node

    def _get_predecessor(self, node):
        while not node.is_leaf:
            node = node.children[-1]
        return node.keys[-1]

    def level_order(self):
        if not self.root:
            return "Empty"
        result = []
        q = deque([self.root])
        while q:
            node = q.popleft()
            result.extend(node.keys)
            for child in node.children:
                q.append(child)
        return ' '.join(map(str, result))

# === Driver Code ===
n, t = map(int, input().split())
keys = list(map(int, input().split()))
q = int(input())
delete_keys = list(map(int, input().split()))

btree = BTree(t)
for key in keys:
    btree.insert(key)

for key in delete_keys:
    btree.delete(key)
    print(btree.level_order())
