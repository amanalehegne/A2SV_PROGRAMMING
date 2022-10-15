class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_sum = 0
        count = i = -2
        while i >= -len(piles) and i >= (count * len(piles) // 3):
            max_sum += piles[i]
            i -= 2
        return max_sum