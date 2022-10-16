class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 2
        for i in range(2, len(nums)):
            # It is always to use greater comparison for sorted elements, especially if you are swapping
            # because, once you swap you lost order, e.g [0,1,1,1,1,2,2] => [0,1,1,2,1,2,3,3]
            # if you compare the index[4] to index[6] using equal, it becomes valid. Which we don't want,
            # but if we compare them using >, we can see it's not valid
            if nums[i] > nums[index-2]:
                nums[index] = nums[i]
                index += 1
        return index