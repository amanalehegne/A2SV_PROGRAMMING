class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[l]:
                return True
            l += 1
        return False