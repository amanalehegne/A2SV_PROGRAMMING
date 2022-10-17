class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for non_zero in range(1, len(nums)):
            if nums[non_zero] == 0:
                if nums[zero] != 0:
                    zero += 1
                continue
            else:
                if nums[zero] == 0:
                    temp = nums[zero]
                    nums[zero] = nums[non_zero]
                    nums[non_zero] = temp
                zero += 1
        