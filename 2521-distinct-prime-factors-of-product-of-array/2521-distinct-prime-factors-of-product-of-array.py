class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primeFactor(num):
            i = 2
            res = set()
            while i * i <= num:
                while num % i == 0:
                    res.add(i)
                    num //= i
                i += 1
            if num != 1:
                res.add(num)
            return list(res)
        
        res = []
        for i in nums:
            res += primeFactor(i)
        
        return len(set(res))
        