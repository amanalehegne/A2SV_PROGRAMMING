class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = [0] * len(nums)
        for i in range(len(nums)):
            index = (i + k) % len(nums)
            temp[index] = nums[i]
        nums[:] = temp
        