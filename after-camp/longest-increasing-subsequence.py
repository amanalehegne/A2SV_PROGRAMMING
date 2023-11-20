class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1] * size
        res = 1

        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
        
        return res
