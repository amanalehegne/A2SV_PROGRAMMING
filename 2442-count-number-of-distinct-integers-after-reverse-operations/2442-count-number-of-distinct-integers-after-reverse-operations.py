class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        sets = set()
        length = len(nums)
        for i in range(length):
            reverse = self.reverse(nums[i])
            nums.append(reverse)

        return len(set(nums))


    def reverse(self, num):
        res = 0
        while num:
            res = res*10 + num%10
            num //= 10
        return res
        