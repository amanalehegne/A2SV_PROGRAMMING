class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, val in enumerate(nums):
            if dic.get(val):
                return [dic[val] - 1, i]
            else:
                dic[target - val] = i + 1