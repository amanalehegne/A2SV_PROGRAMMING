class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        count = 0
        nums.sort()
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            # Adding the largest number to the smallest number yield a higher number than the target,
            # Then there is no other number added with the largest number that would give us the target,
            # Any other number added with the largest would result in an even higher number

            # The same is true for the smallest,
            # If the smallest added with the greatest yield a smaller number than the target
            # There is no other number that when added resulted in a larger number,
            # Thus when this situation came, we remove them from the list
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1

        return count