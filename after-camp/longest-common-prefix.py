class Solution:
    def longestCommonPrefix(self, strs):
        temp = [i for i in strs[0]]
        for word in strs[1:]:
            i = 0
            if len(temp) > len(word):
                temp = temp[:len(word)]
            while i < len(temp) and i < len(word):
                if temp[i] != word[i]:
                    temp = temp[:i]
                    break
                i += 1
        return "".join(temp)
        
