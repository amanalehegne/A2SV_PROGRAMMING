class Solution:
    def longestCommonPrefix(self, strs):
        prefix = list(strs[0])
        length = len(strs)
        for i in range(1, length):
            word = strs[i]
            wordLength = len(word)
            prefixLength = len(prefix)
            index = 0
            while (index < wordLength and index < prefixLength) and (word[index] == prefix[index]):
                index += 1
            prefix = prefix[:index]
        return "".join(prefix)
        
