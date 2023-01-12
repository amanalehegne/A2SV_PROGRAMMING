class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                
        res = [0] * length
        index = 0
        for i in range(length):
            if nums[i]:
                res[index] = nums[i]
                index += 1
        
        return res