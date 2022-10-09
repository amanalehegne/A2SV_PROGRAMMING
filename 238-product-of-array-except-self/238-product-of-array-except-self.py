class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero = 1, False
        ans = [0 for i in range(len(nums))]
        for i, val in enumerate(nums):
            if not zero and val == 0:
                zero = True
                index = i
            elif zero and val == 0:
                return ans
            else:
                product *= val
        if zero:
            ans[index] = product
        else:
            for i in range(len(ans)):
                ans[i] = product // nums[i]
        return ans