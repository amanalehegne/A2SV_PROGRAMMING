class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = []
        for i in s:
            if i.isdigit() or i.isalpha():
                ans.append(i)
        l, r = 0, len(ans) - 1
        while l < r:
            if ans[l] != ans[r]:
                return False
            l += 1
            r -= 1
        return True