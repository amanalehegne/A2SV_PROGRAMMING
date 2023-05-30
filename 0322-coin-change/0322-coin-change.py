class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(x, coins, dic):
            if x in dic:
                return dic[x]
            
            res = float('inf')
            for coin in coins:
                if x - coin >= 0:
                    res = min(res, rec(x - coin, coins, dic))
            dic[x] = res + 1
            return dic[x]
            
        
        res = rec(amount, coins, {0: 0})
        if res == float('inf'):
            res = -1
        return res