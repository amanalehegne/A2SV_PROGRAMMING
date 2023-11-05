class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumValue = dict()
        for i, num in enumerate(nums):
            sumValue[(target - num)] = i + 1

        for i, num in enumerate(nums):
            if sumValue.get(num) and sumValue.get(num) != i + 1:
                return [i, sumValue.get(num) - 1]