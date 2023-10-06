class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]

        for i in range(size1):
            for j in range(size2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-2][-2]