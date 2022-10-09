class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = dict()
        for i, val in enumerate(s):
            dic[val] = i
        l = size = 0
        ans = []
        for i, val in enumerate(s):
            size = max(size, dic.get(val))
            if size == i:
                ans.append(i - l + 1)
                l = i + 1
                size = 0
        return ans