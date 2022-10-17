class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sumVal = 0
        for i in chalk:
            sumVal += i
        k = k % sumVal
        for i, val in enumerate(chalk):
            if k < val:
                return i
            k -= val