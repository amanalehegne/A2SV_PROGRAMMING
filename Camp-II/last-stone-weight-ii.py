class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def dp(idx, res, target, memo):
            if idx >= len(stones) or res >= target:
                return res
            
            if (res, idx) in memo:
                return memo[(res, idx)]
            take = 0
            if res + stones[idx] <= target:
                take = dp(idx + 1, res + stones[idx], target, memo)
            noTake = dp(idx + 1, res, target, memo)
            
            memo[(res, idx)] = max(take, noTake)
            
            return memo[(res, idx)]

        prefix = sum(stones)
        val = ceil(prefix / 2)
        val2 = dp(0, 0, val, {})
        return abs(prefix - val2 - val2)