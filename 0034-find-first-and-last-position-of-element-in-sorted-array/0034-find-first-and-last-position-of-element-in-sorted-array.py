class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftBisect(nums, target):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                midPoint = left + (right - left) // 2
                
                if nums[midPoint] >= target:
                    right = midPoint - 1
                else:
                    left = midPoint + 1
                
            return left
        
        left = leftBisect(nums, target)
        right = leftBisect(nums, target + 1) - 1 

        if left > right:
            return [-1, -1]
        
        return [left, right]
                    
            