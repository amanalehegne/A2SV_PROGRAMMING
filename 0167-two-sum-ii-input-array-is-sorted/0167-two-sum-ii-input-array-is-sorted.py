class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            temp = nums[l] + nums[r]
            if temp == target:
                return [l+1, r+1]
            elif temp > target:
                r -= 1
            else:
                l += 1
        return []