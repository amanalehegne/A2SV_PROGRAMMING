class TrieNode:
    def __init__(self):
        self.children = dict()
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            node.count += 1

    def search(self, word):
        node = self.root
        res = 0
        for char in word:
            node = node.children[char]
            res += node.count
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
      trie = Trie()
      for word in words:
          trie.insert(word)
      res = []
      for word in words:
          res.append(trie.search(word))
        
      return res
              