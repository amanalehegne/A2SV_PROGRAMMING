class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def condition(mid, length):
            subArray = sumVal = 0
            for i in range(length - 1):
                sumVal += nums[i]
                if sumVal + nums[i + 1] > mid:
                    subArray += 1
                    sumVal = 0
            
            return subArray < k
        
        
        left = max(nums)
        right = sum(nums)
        length = len(nums)
        
        while left <= right:
            midPoint = left + (right - left) // 2
            
            if condition(midPoint, length):
                right = midPoint - 1
            else:
                left = midPoint + 1
        
        return left
        