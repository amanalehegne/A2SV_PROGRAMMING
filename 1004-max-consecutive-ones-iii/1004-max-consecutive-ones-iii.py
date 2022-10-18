class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        count = 0
        while r < len(nums):
            if nums[r] != 0 or (nums[r] == 0 and k > 0):
                if nums[r] == 0:
                    k -= 1
                r += 1
            else:
                count = max(count, r - l)
                if nums[l] == 0:
                    k += 1
                l += 1
        return max(count, r - l)