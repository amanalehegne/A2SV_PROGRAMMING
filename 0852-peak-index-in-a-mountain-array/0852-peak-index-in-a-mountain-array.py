class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            midPoint = left + (right - left) // 2
            
            if arr[midPoint] > arr[midPoint + 1]:
                right = midPoint - 1
            else:
                left = midPoint + 1
        
        return left
        
        
                