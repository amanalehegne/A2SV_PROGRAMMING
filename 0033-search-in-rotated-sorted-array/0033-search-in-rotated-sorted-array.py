class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            midPoint = left + (right - left) // 2
            if target == nums[midPoint]:
                return midPoint
            if target > nums[midPoint]:
                # If the middle point is in the rotated portion and
                # the target is greater than the largest element from the regular part (right side of the search space)
                if nums[midPoint] > nums[right]:
                    left = midPoint + 1
                else:
                    if target > nums[right]:
                        right = midPoint - 1
                    else:
                        left = midPoint + 1
            else:
                if nums[midPoint] > nums[right]:
                    if target > nums[right]:
                        right = midPoint - 1
                    else:
                        left = midPoint + 1
                else:
                    right = midPoint - 1
                    
        return -1
        