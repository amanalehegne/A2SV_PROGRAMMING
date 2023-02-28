class Solution:
    def calc(self, x, n, modVal):
        if not x: return 0
        if not n: return 1
        
        res = self.calc(x, n // 2, modVal)
        res = res * res
        
        if n % 2:
            return (res * x) % modVal
        else:
            return res % modVal
        
        
    def countGoodNumbers(self, n: int) -> int:
        modVal = 10 ** 9 + 7
        primeCount = n // 2
        evenCount = n - primeCount
        
        prime = self.calc(4, primeCount, modVal)
        even = self.calc(5, evenCount, modVal)

        return (prime * even) % (modVal)
        