class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        # If we find a double value and its first element is on even index we know that it is pased the single value
        length = len(arr)
        left = 0
        right = length - 1
        if length < 3:
            return arr[0]
        
        while left <= right:
            midPoint = left + (right - left) // 2
            condition1 = midPoint + 1 < length and (arr[midPoint] == arr[midPoint + 1])
            condition2 = midPoint > 0 and (arr[midPoint] == arr[midPoint - 1])
            
            if not condition1 and not condition2:
                return arr[midPoint]
            
            if (condition1 and midPoint % 2) or (condition2 and (midPoint - 1) % 2):
                right = midPoint - 1
            else:
                left = midPoint + 1
                