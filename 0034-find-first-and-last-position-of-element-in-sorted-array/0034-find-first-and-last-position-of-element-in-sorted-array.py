class Solution:
    def searchRange(self, arr: List[int], k: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        res = []
        if not arr:
            return [-1, -1]
        
        while left <= right:
            midPoint = left + (right - left) // 2
            if arr[midPoint] < k:
                left = midPoint + 1
            else:
                right = midPoint - 1
                
        if left >= len(arr) or arr[left] != k:
            left = -1
        res.append(left)
        
        
        left = 0
        right = len(arr) - 1
        while left <= right:
            midPoint = left + (right - left) // 2
            if arr[midPoint] > k:
                right = midPoint - 1
            else:
                left = midPoint + 1
            
        
        if right < 0 or arr[right] != k:
            right = -1
        res.append(right)
    
        return res
        