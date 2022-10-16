class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = dict()
        for i in range(len(s)):
            dic[s[i]] = i

        max_range = 0
        temp = -1
        ans = []
        for i, val in enumerate(s):
            max_range = max(max_range, dic[val])
            if i == max_range:
                ans.append(max_range - temp)
                temp = max_range
        return ans