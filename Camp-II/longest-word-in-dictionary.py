class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for chr in word:
            if chr not in node.children:
                node.children[chr] = TrieNode()
            node = node.children[chr]
        node.isEnd = True

    def search(self, word):
        count = 0
        node = self.root
        for chr in word:
            node = node.children[chr]
            if node.isEnd:
                count += 1
        return count

class Solution:
    def longestWord(self, words: List[str]) -> str:
      trie = Trie()
      for word in words:
        trie.insert(word)
      res = ["", 0]
      for word in words:
        val = trie.search(word)
        if val == len(word):
          if res[-1] < val:
            res = [word, val]
          if res[-1] == val and res[0] > word:
            res = [word, val]
      
      return res[0]
        