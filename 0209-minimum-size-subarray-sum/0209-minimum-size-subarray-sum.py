class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = sumVal = 0
        length = len(nums) + 1
        for i, val in enumerate(nums):
            sumVal += val
            if sumVal >= target:
                while sumVal >= target:
                    length = min(length, i - l + 1)
                    sumVal -= nums[l]
                    l += 1
        return length if length < len(nums) + 1 else 0