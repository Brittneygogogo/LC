# class Trie:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.lookup = {}
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         tree = self.lookup
#         for a in word:
#             if a not in tree:
#                 tree[a] = {}
#             tree = tree[a]
#         # 单词结束标志
#         tree["#"] = "#"
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         tree = self.lookup
#         for a in word:
#             if a not in tree:
#                 return False
#             tree = tree[a]
#         if "#" in tree:
#             return True
#         return False
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         tree = self.lookup
#         for a in prefix:
#             if a not in tree:
#                 return False
#             tree = tree[a]
#         return True


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


'''
class TrieNode:

    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            current = current.children.get(c)
            if current is None:
                return False
        return True

'''
x = Trie()
x.insert("leetcode")
# x.insert("le")
x.insert("leet")
# print(x.lookup)
print(x.search("leet"))