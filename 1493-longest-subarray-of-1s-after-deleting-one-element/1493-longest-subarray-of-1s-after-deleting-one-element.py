class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        check, max_count = True, 0
        l, r = 0, 0
        while r < len(nums):
            if not check and nums[r] == 0:
                max_count = max(max_count,  r - l - 1)
                while l < len(nums) and not check:
                    if nums[l] == 0:
                        check = True
                    l += 1

            if check and nums[r] == 0:
                check = False
            r += 1
        return max(max_count, r - l - 1)