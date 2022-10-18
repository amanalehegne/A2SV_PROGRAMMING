class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = countMax = l = 0
        for i in range(k):
            if s[i] in "aeiou":
                count += 1
        for r in range(i + 1, len(s)):
            countMax = max(countMax, count)
            if s[l] in "aeiou":
                count -= 1
            if s[r] in "aeiou":
                count += 1
            l += 1
        return max(countMax, count)
            