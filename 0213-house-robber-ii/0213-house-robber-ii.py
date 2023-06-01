class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(idx, memo, size):
            if idx >= size:
                return 0
            if idx in memo:
                return memo[idx]
            houseOne = rec(idx + 2, memo, size)
            houseTwo = rec(idx + 3, memo, size)
            
            memo[idx] = max(houseOne, houseTwo) + nums[idx]
            return memo[idx]
        
        size = len(nums)
        res = nums[-1]
        res = max(res, rec(0, dict(), size - 1))
        
        memo = dict()
        for i in range(1, 3):
            res = max(res, rec(i, memo, size))
        
        return res