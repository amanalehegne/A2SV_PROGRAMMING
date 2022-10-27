class Solution:
    def longestWPI(self, nums: List[int]) -> int:
        prefix = length = 0
        dic = dict()
        for i, val in enumerate(nums):
            if val > 8: prefix += 1
            else: prefix -= 1
            if prefix > 0:
                length = i + 1
            if prefix - 1 in dic:
                length = max(length, i - dic.get(prefix - 1))
            if dic.get(prefix) is None:
                dic[prefix] = i
        return length