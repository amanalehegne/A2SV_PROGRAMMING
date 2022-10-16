class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = r = 0
        while l <= r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r += 1
            elif nums[l] != 0 and nums[r] != 0:
                l += 1
                r += 1
            else:
                if nums[r] == 0:
                    r += 1
                if nums[l] != 0:
                    l += 1
        return nums
        