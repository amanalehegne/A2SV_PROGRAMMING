class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        l, r = 0, len(nums) - 1
        while l <= r:
            ans.append(nums[l])
            if l != r:
                ans.append(nums[r])
            l += 1
            r -= 1
        return ans