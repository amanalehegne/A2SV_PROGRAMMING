class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        dic = dict()
        temp = dict()
        for i in "abcdefghijklmnopqrstuvwxyz":
            dic[i] = 0
            temp[i] = 0
        for i in p:
            dic[i] += 1

        for r in range(len(p)):
            temp[s[r]] += 1
        l, r = 0, r + 1
        ans = []
        while r < len(s):
            if dic == temp:
                ans.append(l)
            temp[s[l]] -= 1
            temp[s[r]] += 1
            l += 1
            r += 1
        if dic == temp:
            ans.append(l)
        return ans
