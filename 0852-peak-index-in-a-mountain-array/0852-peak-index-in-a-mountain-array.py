class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 1
        high = len(arr) - 2
        res = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
        