class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        tokens.sort()
        score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                l += 1
                score += 1
            else:
                if l < r and score > 0:
                    power += tokens[r]
                    r -= 1
                    score -= 1
                else:
                    return score
        return score