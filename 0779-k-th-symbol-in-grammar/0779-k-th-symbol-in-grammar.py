class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n, k):
            if n == 1 or k == 1:
                return 0
            rowSize = (2 ** (n - 1))
            half = rowSize // 2
            if k <= half:
                # Origional Half
                return helper(n - 1, k)
            else:
                # Inverted Half
                if not helper(n - 1, k - half): return 1
                return 0
        
        return helper(n, k)