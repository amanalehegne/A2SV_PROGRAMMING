class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sindex = 0
        for i in range(1, len(nums)):
            if (nums[sindex] * nums[sindex]) > (nums[i] * nums[i]):
                sindex = i
        ans = []
        l, r = sindex, sindex + 1
        while r < len(nums) and l >= 0:
            if (nums[r] * nums[r]) > (nums[l] * nums[l]):
                ans.append(nums[l] * nums[l])
                l -= 1
            else:
                ans.append(nums[r] * nums[r])
                r += 1
        while r < len(nums):
            ans.append(nums[r] * nums[r])
            r += 1
        while l >= 0:
            ans.append(nums[l] * nums[l])
            l -= 1
        return ans