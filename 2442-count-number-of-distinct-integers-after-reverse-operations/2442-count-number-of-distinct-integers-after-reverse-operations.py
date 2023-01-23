class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        sets = set()
        length = len(nums)
        for i in range(length):
            sets.add(nums[i])
            sets.add(self.reverse(nums[i]))

        return len(sets)


    def reverse(self, num):
        res = 0
        while num:
            res = res*10 + num%10
            num //= 10
        return res
        