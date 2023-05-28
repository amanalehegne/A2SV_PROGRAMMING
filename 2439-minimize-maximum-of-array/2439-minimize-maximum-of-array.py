class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        size = len(nums)
        val = sum(nums)
        
        for i in range(size - 1):
            idx = size - 1 - i
            currentVal = ceil(val / (idx + 1))
            if nums[idx] > currentVal:
                temp = nums[idx] - currentVal
                nums[idx] -= temp
                nums[idx - 1] += temp
            
            val -= nums[idx]
        
        return max(nums)