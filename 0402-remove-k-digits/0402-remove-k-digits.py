class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        if len(nums) <= k:
            return "0"
        stack = []
        count = 0
        for i, val in enumerate(nums):
            while stack and stack[-1] > val and count < k:
                stack.pop()
                count += 1
            stack.append(val)
        ans = "".join(stack[0:len(nums) - k])
        return str(int(ans))