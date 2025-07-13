class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Driver Code
n = int(input())
trie = Trie()

for _ in range(n):
    parts = input().split()
    cmd, word = parts[0], parts[1]
    
    if cmd == "insert":
        trie.insert(word)
    elif cmd == "search":
        print("true" if trie.search(word) else "false")
    elif cmd == "startsWith":
        print("true" if trie.startsWith(word) else "false")
