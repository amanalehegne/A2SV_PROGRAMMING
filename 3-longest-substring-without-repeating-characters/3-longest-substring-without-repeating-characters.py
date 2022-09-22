class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length, i = 0, 0
        ans = ""
        dic = {}
        while i < len(s):
            if not dic.get(s[i]):
                ans += s[i]
                dic[s[i]] = True
                i += 1
            else:
                length = max(length, len(ans))
                dic[ans[0]] = False
                ans = ans[1:]
        return max(length, len(ans))