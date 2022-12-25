class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        index = 0
        length = len(nums)
        for i in range(length):
            if nums[index] % 2:
                if not nums[i] % 2:
                    nums[index], nums[i] = nums[i], nums[index]
                    index += 1
            else:
                index += 1
        
        return nums
        