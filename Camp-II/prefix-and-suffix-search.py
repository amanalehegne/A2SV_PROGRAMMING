class TrieNode:
    def __init__(self):
        self.children = dict()
        self.suffix = defaultdict(int)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx, suffix):
        node = self.root
        size = len(word)
        for i in range(size):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()

            node = node.children[word[i]]
            for val in suffix:
                node.suffix[val] = idx

    def search(self, prefix, suffix):
        node = self.root
        for char in prefix:
          if char not in node.children:
            return -1
          node = node.children[char]

        if suffix not in node.suffix:
            return -1
        return node.suffix[suffix]
      
    def findSuffix(self, word):
      suffix = []
      for i in range(len(word)):
          suffix.append(word[i:])

      return suffix

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        size = len(words)
        for i in range(size):
          suffix = self.trie.findSuffix(words[i])
          self.trie.insert(words[i], i, suffix)

    def f(self, pref: str, suff: str) -> int:
      return self.trie.search(pref, suff)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)