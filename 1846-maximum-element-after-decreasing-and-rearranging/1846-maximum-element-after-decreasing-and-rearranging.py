class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        size = len(arr)
        
        arr[0] = 1
        for i in range(size - 1):
            if arr[i + 1] - arr[i] > 1:
                arr[i + 1] = (arr[i] + 1)
        
        return max(arr)
        