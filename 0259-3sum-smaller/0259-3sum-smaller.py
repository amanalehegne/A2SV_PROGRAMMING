class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count