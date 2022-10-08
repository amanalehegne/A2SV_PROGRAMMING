class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flip = 0
        l, r = 0, 0
        long = 0
        while r < len(nums):
            if flip == k and nums[r] == 0:
                long = max(long, r - l)
                while flip >= k:
                    if nums[l] == 0:
                        flip -= 1
                    l += 1
            if nums[r] == 0:
                flip += 1
                r += 1
            elif nums[r] == 1:
                r += 1
        return max(long, r - l)