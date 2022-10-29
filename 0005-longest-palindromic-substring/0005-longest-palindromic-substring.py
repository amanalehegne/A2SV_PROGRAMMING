class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        length = ""
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(length) < r - l + 1:
                    length = s[l:r+1]
                r += 1
                l -= 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(length) < r - l + 1:
                    length = s[l:r+1]
                r += 1
                l -= 1
        return length