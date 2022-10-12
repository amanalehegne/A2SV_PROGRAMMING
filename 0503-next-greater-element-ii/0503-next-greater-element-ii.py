class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i in range(len(nums) * 2):
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                ans[stack.pop()] = nums[i % len(nums)]
            if i < len(nums):
                stack.append(i)
        return ans