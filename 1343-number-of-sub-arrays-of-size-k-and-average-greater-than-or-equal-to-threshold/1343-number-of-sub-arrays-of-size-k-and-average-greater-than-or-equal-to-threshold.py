class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count, window_sum, l = 0, 0, 0
        for r, val in enumerate(arr):
            window_sum += val
            if r >= k - 1:
                if window_sum / k >= threshold:
                    count += 1
                window_sum -= arr[l]
                l += 1
        return count