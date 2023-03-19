class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            midPoint = left + (right - left) // 2
            if target == nums[midPoint]:
                return True
            if nums[left] == nums[midPoint] and nums[midPoint] == nums[right]:
                left += 1
                right -= 1
            elif target > nums[midPoint]:
                if (nums[midPoint] > nums[right]) or (target <= nums[right]):
                    left = midPoint + 1
                else:
                    right = midPoint - 1
            else:
                if nums[midPoint] > nums[right]:
                    if target > nums[right]:
                        right = midPoint - 1
                    else:
                        left = midPoint + 1
                else:
                    right = midPoint - 1

        return False
        