class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumTotal = maxVal = None
        for r in range(k):
            if sumTotal is None:
                sumTotal = nums[r]
            else:
                sumTotal += nums[r]
        l = 0
        for i in range(r + 1, len(nums)):
            if maxVal is None:
                maxVal = sumTotal / k
            else:
                maxVal = max(maxVal, sumTotal / k)
            sumTotal -= nums[l] - nums[i]
            l += 1
        if maxVal is None:
            return sumTotal / k
        return max(maxVal, sumTotal / k)