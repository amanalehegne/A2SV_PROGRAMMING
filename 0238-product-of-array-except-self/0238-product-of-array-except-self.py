class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        prefix, zindex = 1, -1
        for i, val in enumerate(nums):
            if val == 0:
                if zindex >= 0:
                    return ans
                zindex = i
            else:
                prefix *= val
        if zindex >= 0:
            ans[zindex] = prefix
        else:
            for i, val in enumerate(nums):
                ans[i] = prefix // val
        return ans