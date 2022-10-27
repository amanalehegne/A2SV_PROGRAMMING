class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = length = 0
        dic = dict()
        for i, val in enumerate(nums):
            if val: prefix += 1
            else: prefix -= 1
            if prefix == 0:
                length = max(length, i + 1)
            if dic.get(prefix) is not None:
                length = max(length, i - dic.get(prefix))
            if dic.get(prefix) is None:
                dic[prefix] = i
        return length