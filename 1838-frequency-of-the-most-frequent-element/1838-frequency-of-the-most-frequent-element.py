class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = len(nums)
        left = res = 0
        windowSum = 0
        
        for i in range(length):
            windowSum += nums[i]
            maxVal = nums[i]
            
            while (windowSum + k) < (maxVal * (i - left + 1)):
                windowSum -= nums[left]
                left += 1
            
            res = max(res, i - left + 1)
        
        return res
            
                