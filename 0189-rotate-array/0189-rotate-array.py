class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        temp = nums[len(nums) - k:]
        for i in range(len(nums) - k):
            nums[-1-i] = nums[-k-1-i]
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        