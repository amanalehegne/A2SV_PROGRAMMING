class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, number, binary):
        node = self.root
        for char in binary:
            if char not in node:
                node[char] = dict()
            node = node[char]
        node["val"] = number

    def search(self, number, binary):
        node = self.root
        for char in binary:
            val = str(1 - int(char))
            if val in node:
                node = node[val]
            else:
                node = node[char]
        return number ^ node["val"]

class Solution:

    def binary(self, number):
        binary = bin(number)[2:]
        return binary.zfill(32)

    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            temp = self.binary(num)
            trie.insert(num, temp)
        res = 0
        for num in nums:
            temp = self.binary(num)
            res = max(res, trie.search(num, temp))
        
        return res
        