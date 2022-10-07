class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(nums):
            if not dic.get(val):
                dic[target - val] = [val, i]
            else:
                return [dic.get(val)[1], i]
        return []