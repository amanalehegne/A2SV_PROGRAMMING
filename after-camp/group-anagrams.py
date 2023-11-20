class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for i in strs:
            temp = sorted(i)
            temp = "".join(temp)
            if dic.get(temp):
                dic[temp].append(i)
            else:
                dic[temp] = [i]
        return dic.values()