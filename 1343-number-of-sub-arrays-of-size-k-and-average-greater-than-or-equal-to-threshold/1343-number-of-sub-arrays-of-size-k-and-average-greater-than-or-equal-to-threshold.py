class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = count = l = 0
        for i in range(k):
            window += arr[i]
        for r in range(i + 1, len(arr) + 1):
            if window / k >= threshold:
                count += 1
            if r < len(arr):
                window -= arr[l] - arr[r]
                l += 1
        return count