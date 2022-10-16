class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        print(nums)
        for i, val in enumerate(nums):
            # Handle duplicate elements - by removing them
            if i > 0 and val == nums[i - 1]:
                continue
            # Find two sum that when added to current value gives us 0
            l, r = i+1, len(nums) - 1
            while l < r:
                temp = nums[l] + nums[r]
                if temp > 0 - val:
                    r -= 1
                elif temp < 0 - val:
                    l += 1
                else:
                    ans.append([val, nums[l], nums[r]])
                    l += 1
                    # If the shifted value is similar to the previous value, then it's duplicate
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans