class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums) and nums[i] <= target:
            if nums[i] == target:
                ans.append(i)
            i += 1
        return ans