class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        if len(tokens) == 0 or tokens[0] > power:
            return score
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