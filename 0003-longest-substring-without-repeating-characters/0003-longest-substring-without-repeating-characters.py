class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = count = 0
        dic = dict()
        while r < len(s):
            if not dic.get(s[r]):
                dic[s[r]] = True
                r += 1
            else:
                count = max(count, r - l)
                dic[s[l]] = False
                l += 1
        return max(count, r - l)
        