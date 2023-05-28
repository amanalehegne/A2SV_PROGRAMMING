class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        size = len(nums)
        sum_ = res = 0
        
        for i in range(size):
            sum_ += nums[i]
            res = max(res, ceil(sum_ / (i + 1)))
            
        
        return res