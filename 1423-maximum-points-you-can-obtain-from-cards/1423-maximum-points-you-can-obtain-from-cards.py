class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = 0
        for i in range(len(cardPoints) - k, len(cardPoints)):
                total_sum += cardPoints[i]
        l, r = 0, len(cardPoints) - k
        total_max = total_sum
        while r < len(cardPoints):
            total_sum += cardPoints[l] - cardPoints[r]
            total_max = max(total_sum, total_max)
            l += 1
            r += 1
        return total_max