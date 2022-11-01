class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for r in range(1, len(nums)):
            l = r - 1
            if nums[r] - nums[l] > 1:
                return nums[l] + 1
        if nums[0] != 0:
            return 0
        return nums[-1] + 1