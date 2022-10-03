class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            val = nums[i]
            # Greater because, it's sorted in ascending order, and if the next element is smaller
            # there is a chance that it came in the previous one and thus not unique
            # 1, 2, 2, 2 => 1, 2, 3, 2 , our current element is 2, and the previous one is 3,
            # 2 < 3 means there is a chance it came before, and in this case it did!
            if prev >= val:
                count += prev - val + 1
                nums[i] = prev + 1
        print(nums)
        return count