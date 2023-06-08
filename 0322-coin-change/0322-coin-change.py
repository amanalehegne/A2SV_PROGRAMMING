class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(x, coins, dic):
            if x in dic:
                return dic[x]
            if x < 0:
                return float('inf')
            if x == 0:
                return 0
            res = float('inf')
            for coin in coins:
                res = min(res, rec(x - coin, coins, dic))

            dic[x] = res + 1
            return dic[x]
            
        
        res = rec(amount, coins, dict())
        if res == float('inf'):
            res = -1
        return res