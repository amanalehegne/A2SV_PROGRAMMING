class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes + numZeros >= k:
            return min(k, numOnes)
        else:
            remaining = k - (numOnes + numZeros)
            return numOnes - remaining