class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def rec(idx, memo):
            if idx >= len(cost) - 2:
                return cost[idx]
            
            if idx in memo:
                return memo[idx]
            
            one = rec(idx + 1, memo)
            two = rec(idx + 2, memo)
            
            memo[idx] = min(one, two) + cost[idx]
            
            return memo[idx]
        
        memo = dict()
        return min(rec(0, memo), rec(1, memo))
        