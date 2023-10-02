class TrieNode:
    def __init__(self):
        self.children = dict()


class Trie:
    def __init__(self, word):
        self.root = TrieNode()
        self.dic = defaultdict(list)
        size = len(word)
        for i in range(size):
            self.dic[word[i]].append(i)

    def insert(self, word):
        node = self.root
        for chr in word:
            if chr not in node.children:
                node.children[chr] = TrieNode()
            node = node.children[chr]

    def search(self, word):
        node = self.root
        idx = -1
        for chr in word:
            tmp = bisect_left(self.dic[chr], idx)
            if tmp == len(self.dic[chr]) or (idx > self.dic[chr][tmp]):
                return False
            idx = self.dic[chr][tmp] + 1
            node = node.children[chr]
        return True
              

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie(s)
        for word in words:
            trie.insert(word)

        count = 0
        for word in words:
            if trie.search(word):
                count += 1
        
        return count