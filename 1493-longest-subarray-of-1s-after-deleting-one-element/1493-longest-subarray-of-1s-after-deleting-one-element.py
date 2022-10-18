class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = -1
        l = r = count = 0
        while r < len(nums):
            if nums[r] == 0 and zero < l:
                zero = r
                r += 1
            elif nums[r] == 0 and zero >= l:
                count = max(count, r - l - 1)
                l = zero + 1
            else:
                r += 1
        return max(count, r - l - 1)