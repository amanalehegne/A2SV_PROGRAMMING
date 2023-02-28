class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        length = len(nums)
        kValue = -float("inf")
        for i in range(length):
            idx = length - 1 - i
            if nums[idx] < kValue:
                return True
            while stack and stack[-1] < nums[idx]:
                kValue = stack.pop()
                
            stack.append(nums[idx])
        return False