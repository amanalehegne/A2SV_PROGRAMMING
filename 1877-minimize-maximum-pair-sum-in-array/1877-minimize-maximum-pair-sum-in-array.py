class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair = 0
        for i in range(1, len(nums) + 1):
            max_pair = max(max_pair, nums[i - 1] + nums[-i])
        return max_pair