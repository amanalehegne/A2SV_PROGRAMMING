class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        prefix = 1
        zero, zindex = 0, -1
        for i, val in enumerate(nums):
            if val == 0:
                zero += 1
                zindex = i
            else:
                prefix *= val
            if zero > 1:
                return ans
        if zindex >= 0:
            ans[zindex] = prefix
        else:
            for i, val in enumerate(nums):
                ans[i] = prefix // val
        return ans