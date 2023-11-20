class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        length = len(nums)
        jValue = -float("inf")
        for i in range(length):
            idx = length - 1 - i
            if nums[idx] < jValue:
                return True
            while stack and stack[-1] < nums[idx]:
                jValue = stack.pop()
                
            stack.append(nums[idx])
        return False