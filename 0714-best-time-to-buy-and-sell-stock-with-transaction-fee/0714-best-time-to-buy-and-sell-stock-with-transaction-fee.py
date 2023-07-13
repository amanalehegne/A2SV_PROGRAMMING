class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        profit = 0
        price = prices[0]

        for i in range(1, size):
            transaction = prices[i] - price - fee
            profit = max(profit, transaction)
            price = min(price, prices[i] - profit)
        
        print(profit, price)
        return profit