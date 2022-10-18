class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        dic = dict()
        temp = dict()
        for i in p:
            if dic.get(i) is not None:
                dic[i] += 1
            else:
                dic[i] = 1

        for r in range(len(p)):
            if temp.get(s[r]) is not None:
                temp[s[r]] += 1
            else:
                temp[s[r]] = 1
        l, r = 0, r + 1
        ans = []
        while r < len(s):
            if self.compareMaps(dic, temp):
                ans.append(l)
            temp[s[l]] -= 1
            if temp[s[l]] == 0:
                temp.pop(s[l])
            if temp.get(s[r]) is not None:
                temp[s[r]] += 1
            else:
                temp[s[r]] = 1
            l += 1
            r += 1
        if self.compareMaps(dic, temp):
            ans.append(l)
        return ans
    
    def compareMaps(self, dic1, dic2):
        for key in dic1:
            if dic2.get(key) is None:
                return False
            if dic1[key] != dic2[key]:
                return False
        return True
