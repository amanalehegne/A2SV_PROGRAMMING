class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        
        for i in range(size):
            if nums[i] < 1 or nums[i] > size:
                nums[i] = float('inf')

        for i in range(size):
            num = abs(nums[i])
            if num < float('inf'):
                nums[num - 1] = -1 * abs(nums[num - 1])

        for i in range(size):
            if nums[i] > 0:
                return i + 1

        return size + 1
