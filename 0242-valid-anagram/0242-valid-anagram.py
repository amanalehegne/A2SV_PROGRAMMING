class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict()
        for i in s:
            dic[i] = 1 + dic.get(i, 0)
        for i in t:
            if not dic.get(i):
                return False
            dic[i] -= 1
            if dic.get(i) == 0:
                dic.pop(i)
        if dic:
            return False
        return True