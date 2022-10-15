class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev != nums[i]:
                nums[index] = nums[i]
                prev = nums[i]
                index += 1
        return index