class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        idx1 = idx2 = 0
        length1 = len(word1)
        length2 = len(word2)
        res = []
        while idx1 < length1 and idx2 < length2:
            if word1[idx1:] > word2[idx2:]:
                res.append(word1[idx1])
                idx1 += 1
            else:
                res.append(word2[idx2])
                idx2 += 1
        while idx1 < length1:
            res.append(word1[idx1])
            idx1 += 1
        while idx2 < length2:
            res.append(word2[idx2])
            idx2 += 1
        
        return "".join(res)

