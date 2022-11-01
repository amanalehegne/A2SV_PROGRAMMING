class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for val in strs:
            temp = [0] * 26
            for i in val:
                temp[ord(i) - ord('a')] += 1
            dic[tuple(temp)].append(val)
        return dic.values()