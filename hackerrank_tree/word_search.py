class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store word at the end node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word  # store full word at end

def findWords(board, words):
    m, n = len(board), len(board[0])
    result = set()
    
    trie = Trie()
    for word in words:
        trie.insert(word)

    def dfs(i, j, node):
        ch = board[i][j]
        if ch not in node.children:
            return
        next_node = node.children[ch]
        if next_node.word:
            result.add(next_node.word)
            next_node.word = None  # prevent duplicate

        board[i][j] = '#'  # mark visited
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                dfs(ni, nj, next_node)
        board[i][j] = ch  # unmark

    for i in range(m):
        for j in range(n):
            dfs(i, j, trie.root)

    return result

# === Driver Code ===
m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(input().split())

k = int(input())
words = [input().strip() for _ in range(k)]

found_words = findWords(board, words)
for word in found_words:
    print(word)
