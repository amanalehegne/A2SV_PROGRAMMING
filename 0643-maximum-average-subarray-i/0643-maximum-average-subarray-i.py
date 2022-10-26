class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumTotal = l = 0
        for r in range(k):
            sumTotal += nums[r]
        maxVal = sumTotal / k
        for i in range(r + 1, len(nums)):
            maxVal = max(maxVal, sumTotal / k)
            sumTotal -= nums[l] - nums[i]
            l += 1
        return max(maxVal, sumTotal / k)