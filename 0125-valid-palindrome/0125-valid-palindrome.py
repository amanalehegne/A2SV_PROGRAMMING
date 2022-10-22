class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if (s[l].isalpha() or s[l].isdigit()) and (s[r].isalpha() or s[r].isdigit()):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            else:
                if (s[l].isalpha() or s[l].isdigit()) and (not s[r].isalpha() and not s[r].isdigit()):
                    r -= 1
                else:
                    l += 1
        return True