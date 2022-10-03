class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total = 0
        minimum = len(nums) + 1
        while r < len(nums):
            total += nums[r]
            if total >= target:
                while total >= target and l <= r:
                    minimum = min(minimum, r - l + 1)
                    total -= nums[l]
                    l += 1
            r += 1
        if minimum > len(nums):
            return 0
        return minimum