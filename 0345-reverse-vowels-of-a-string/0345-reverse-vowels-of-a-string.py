class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = []
        for i in s:
            ans.append(i)
        l, r = 0, len(ans) - 1
        while l < r:
            if not (ans[l] in "aeiouAEIOU"):
                l += 1
            if not (ans[r] in "aeiouAEIOU"):
                r -= 1
            if ans[l] in "aeiouAEIOU" and ans[r] in "aeiouAEIOU":
                temp = ans[l]
                ans[l] = ans[r]
                ans[r] = temp
                l += 1
                r -= 1
        return "".join(ans)