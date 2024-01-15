class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        length = min(len(s), len(t))
        editCount = 0

        if len(s) == len(t):
            for i in range(length):
                if s[i] != t[i]:
                    editCount += 1
            return editCount == 1

        if abs(len(s) - len(t)) == 1:
            i, j = 0, 0

            while i < len(s) and j < len(t) and s[i] == t[j]:
                i += 1
                j += 1

            return s[i:] == t[j+1:] or s[i+1:] == t[j:]

        return False
