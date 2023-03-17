class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        res = float("inf")
        
        while left <= right:
            midPoint = left + (right - left) // 2
            
            res = min(res, nums[midPoint])
            if nums[midPoint] > nums[right]:
                left = midPoint + 1
            else:
                right = midPoint - 1
        
        return res
                