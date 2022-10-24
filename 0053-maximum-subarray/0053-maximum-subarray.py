class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        l = window = 0
        ans = arr[0]
        for val in arr:
            if window < 0:
                window = 0
            window += val
            ans = max(ans, window)
        return max(ans, window)