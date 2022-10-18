class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = window = r = l = maxScore = 0
        for i, val in enumerate(cardPoints):
            total += val
            if i == len(cardPoints) - k - 1:
                window = total
                r = i + 1
        for i in range(r, len(cardPoints)):
            maxScore = max(maxScore, total - window)
            window -= cardPoints[l] - cardPoints[i]
            l += 1
        return max(maxScore, total - window)