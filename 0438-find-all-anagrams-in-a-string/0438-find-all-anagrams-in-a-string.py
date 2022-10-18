class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) >= len(p):
            dic, temp = dict(), dict()
            for i in p:
                dic[i] = 1 + dic.get(i, 0)
            for r in range(len(p)):
                temp[s[r]] = 1 + temp.get(s[r], 0)
            l, r, ans = 0, r + 1, []
            while r < len(s):
                if self.compareMaps(dic, temp):
                    ans.append(l)
                temp[s[l]] -= 1
                if temp[s[l]] == 0:
                    temp.pop(s[l])
                temp[s[r]] = 1 + temp.get(s[r], 0)
                l, r = l+1, r+1
            if self.compareMaps(dic, temp):
                ans.append(l)
            return ans
    
    def compareMaps(self, dic1, dic2):
        for key in dic1:
            if (dic2.get(key) is None) or (dic1[key] != dic2[key]):
                return False
        return True
