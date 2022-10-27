class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = l = r = 0
        product = 1
        while r < len(nums):
            product *= nums[r]
            while product >= k:
                if l > r: return count
                product //= nums[l]
                l += 1
            if product < k:
                count += (r - l + 1)
            r += 1
        return count
        