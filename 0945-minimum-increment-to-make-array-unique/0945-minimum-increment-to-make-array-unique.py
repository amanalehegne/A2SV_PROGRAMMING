class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for r in range(1, len(nums)):
            if nums[r - 1] >= nums[r]:
                count += nums[r - 1] + 1 - nums[r]
                nums[r] = nums[r - 1] + 1
        return count