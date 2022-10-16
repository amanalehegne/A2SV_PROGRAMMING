class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = max_sub = 0
        dic = dict()
        while r < len(s):
            if not dic.get(s[r]):
                dic[s[r]] = True
                r += 1
            else:
                max_sub = max(max_sub, r - l)
                dic[s[l]] = False
                l += 1
        return max(max_sub, r - l)